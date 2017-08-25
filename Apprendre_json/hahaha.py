import json

data = {"err": 44, "eds": 56}

with open("test.json", "w") as file:
    json.dump(data, file, indent=4)
