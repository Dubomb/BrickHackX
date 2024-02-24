import json

path = "data/goals.json"

def write_goal(goal):
    print("Writing goal")

    with open(path, "r") as f:
        data = json.load(f)
        data.append(json.loads(goal))

    with open(path, "w") as f:
        json.dump(data, f)

def read_goals():
    print("Reading goal")

    with open(path, "r") as f:
        data = json.load(f)

    return data