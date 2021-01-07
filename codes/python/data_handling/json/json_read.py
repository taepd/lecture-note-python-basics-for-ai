import json

with open("json_example.json", "r", encoding="utf8") as f:
    contents = f.read()
    json_data = json.loads(contents)
print(type(json_data))
for employee in json_data["employees"]:
    print(employee["lastName"])
