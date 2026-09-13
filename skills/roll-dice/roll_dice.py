#!/usr/bin/env python3
import random
import re
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    print(f"Rolling {sys.argv[1]}...")
        
    match = re.search(r'(\d+)?d(\d+)([+-]\d+)?', sys.argv[1].replace(" ", ""))
    if not match:
        sys.exit(1)
        
    num = int(match.group(1) or 1)
    sides = int(match.group(2))
    mod = int(match.group(3) or 0)

    rolls = [random.randint(1, sides) for _ in range(num)]
    total = sum(rolls) + mod
    
    rolls_str = " + ".join(map(str, rolls))
    if mod > 0:
        print(f"{rolls_str} + {mod} = {total}")
    elif mod < 0:
        print(f"{rolls_str} - {abs(mod)} = {total}")
    else:
        if num > 1:
            print(f"{rolls_str} = {total}")
        else:
            print(total)

if __name__ == "__main__":
    main()
