#!/usr/bin/python3
import json, subprocess

CONFIG_FILE = "/home/mechatronics/install/install/launch/startupConfig.json"

with open(CONFIG_FILE, 'r') as file:
    data = json.load(file)

for script in data.get('scripts', []):
    print("NACJAC")
    # subprocess.run(script.get("command"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process = subprocess.Popen(script.get("command"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print("Eat shit and die")
