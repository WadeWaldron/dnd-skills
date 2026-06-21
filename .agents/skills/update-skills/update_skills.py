import os
import shutil
import urllib.request
import zipfile
import tempfile
import sys

def update_skills():
    repo_url = "https://github.com/WadeWaldron/dnd-skills/archive/refs/heads/main.zip"
    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, "repo.zip")

    print(f"Downloading latest skills from {repo_url}...")
    try:
        # Use a user-agent to avoid potential blocks
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(repo_url, zip_path)
    except Exception as e:
        print(f"Error downloading: {e}")
        shutil.rmtree(temp_dir)
        return

    print("Extracting files...")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
    except Exception as e:
        print(f"Error extracting: {e}")
        shutil.rmtree(temp_dir)
        return

    # Find the .agents folder in the extracted content
    source_agents = None
    for root, dirs, files in os.walk(temp_dir):
        if ".agents" in dirs:
            source_agents = os.path.join(root, ".agents")
            break

    if not source_agents:
        print("Could not find .agents folder in the downloaded repository.")
        shutil.rmtree(temp_dir)
        return

    # Determine workspace root relative to this script
    # Path: .agents/skills/update-skills/update_skills.py
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
    target_agents = os.path.join(workspace_root, ".agents")

    print(f"Updating skills in {target_agents}...")
    
    try:
        # We copy individual items to avoid issues with the currently executing script
        # if it's being replaced.
        for item in os.listdir(source_agents):
            s = os.path.join(source_agents, item)
            d = os.path.join(target_agents, item)
            if os.path.isdir(s):
                if os.path.exists(d):
                    shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        print("Update complete! You may need to refresh your environment to see changes.")
    except Exception as e:
        print(f"Error during update: {e}")
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    update_skills()
