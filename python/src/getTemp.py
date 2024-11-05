import json
import os

current_directory = os.getcwd()

def getTemp():
    with open(f"{current_directory}\\logs\\temp.json", "r") as file:
        return json.load(file)
        