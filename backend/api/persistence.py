import json

path = "data/goals.json"

def read_goals():
    print("Reading goal")

    with open(path, "r") as f:
        data = json.load(f)

    return data

def write_goal(goal):
    print("Writing goal")

    with open(path, "r") as f:
        data = json.load(f)
        data.append(json.loads(goal))

    with open(path, "w") as f:
        json.dump(data, f)

def update_goal(goal):
    print("Update goal")

    goal_json = json.loads(goal)

    with open(path, "r") as f:
        data = json.load(f)

    for d in data:
        if d["id"] == goal_json:
            d = goal_json
    
    for i in range(len(data)):
        if data[i]["id"] == goal_json["id"]:
            data[i] = goal_json
    
    with open(path, "w") as f:
        json.dump(data, f)