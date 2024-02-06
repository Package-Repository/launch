import json, subprocess

CONFIG_FILE = "startupConfig.json"

with open(CONFIG_FILE, 'r') as file:
    data = json.load(file)

for script in data.get('scripts', []):
    try:
        subprocess.run(script.get("command"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except FileNotFoundError as e:
        print(f"Error executing the command for script '{script.get('name')}': {e}")