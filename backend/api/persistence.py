import json

path = "data/goals.json"

def write_goal():
    print("Writing goal")

def read_goals():
    print("Reading goal")

    with open(path, "r") as f:
        data = json.load(f)

    return data