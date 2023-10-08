import json

with open("stations_old.json", "r", encoding="utf-8") as f:
    file = json.load(f)

new_list = {}
for item in file:
    new_list[f"{file[item]['lat']};{file[item]['lon']}"] = file[item]["bundesland"]

with open("development/bundeslaender.json", "w", encoding="utf-8") as f:
    json.dump(new_list, f, ensure_ascii=False)