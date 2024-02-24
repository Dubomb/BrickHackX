
path = "data/goals.json"

def write_goal():
    print("Writing goal")

def read_goals():
    print("Reading goal")

    f = open(path, "r")
    lines = f.readlines()
    print(lines)

    return lines