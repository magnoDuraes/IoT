import json

def getTemp():
    with open("python/app/src/logs/temp.json", "r") as file:
        return json.load(file)
        