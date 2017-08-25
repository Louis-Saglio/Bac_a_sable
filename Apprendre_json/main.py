import json

with open("file.json", "r") as f:
    data = json.load(f)
    print(data)

with open("a.json", "w") as a:
    json.dump(data, a, indent=4)

