import json
import os
import re
import sys

def get_table_widths(table_lines):
    """Calculates ideal widths for a table based on content."""
    # Split by | and strip whitespace
    rows = [[c.strip() for c in l.strip().strip('|').split('|')] for l in table_lines]
    if not rows:
        return []

    num_cols = len(rows[0])
    widths = [0] * num_cols

    for row_idx, row in enumerate(rows):
        # Skip the separator row for width calculation
        if row_idx == 1:
            continue
        for i in range(min(len(row), num_cols)):
            widths[i] = max(widths[i], len(row[i]))

    # Ensure minimum width for MD separator (3 dashes)
    return [max(w, 3) for w in widths]

def format_markdown_table(table_lines):
    """Returns a perfectly formatted list of table lines."""
    widths = get_table_widths(table_lines)
    if not widths:
        return table_lines

    formatted = []
    for row_idx, line in enumerate(table_lines):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        new_row = "|"
        for i, width in enumerate(widths):
            content = cells[i] if i < len(cells) else ""
            if row_idx == 1: # Separator row logic
                left_align = content.startswith(':')
                right_align = content.endswith(':')

                # The internal separator must be exactly 'width' characters long
                if left_align and right_align:
                    sep = ":" + "-" * (width - 2) + ":"
                elif left_align:
                    sep = ":" + "-" * (width - 1)
                elif right_align:
                    sep = "-" * (width - 1) + ":"
                else:
                    sep = "-" * width

                new_row += " " + sep + " |"
            else:
                new_row += " " + content.ljust(width) + " |"
        formatted.append(new_row)
    return formatted


def format_all_tables(text):
    """Realign every Markdown table in `text`. Returns the rewritten text."""
    out, table = [], []
    for line in text.splitlines():
        if line.strip().startswith('|'):
            table.append(line)
            continue
        if len(table) >= 3:
            out.extend(format_markdown_table(table))
        else:
            out.extend(table)
        table = []
        out.append(line)
    if len(table) >= 3:
        out.extend(format_markdown_table(table))
    else:
        out.extend(table)
    return "\n".join(out) + "\n"


def main():
    """PostToolUse hook entry point.

    Reads the hook payload on stdin, finds the file the Write/Edit tool just
    touched, and rewrites any Markdown tables in it with aligned whitespace.
    Does nothing for non-Markdown files, or if the file can't be read or
    written. Always exits 0 - a formatter must never block a write.
    """
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return

    tool_input = payload.get("tool_input") or {}
    tool_response = payload.get("tool_response") or {}

    path = (
        tool_input.get("file_path")
        or tool_response.get("filePath")
        or tool_response.get("file_path")
    )
    if not path or os.path.splitext(path)[1].lower() not in (".md", ".markdown"):
        return

    try:
        with open(path, "r", encoding="utf-8") as fh:
            original = fh.read()
    except OSError:
        return

    formatted = format_all_tables(original)
    if formatted == original:
        return

    try:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(formatted)
    except OSError:
        return


if __name__ == "__main__":
    main()
