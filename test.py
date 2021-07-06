import json
citizens = [
    {"name": "smith", "nationality":"england"},
    {"name": "austin ", "nationality":"australia"}
]

file = open("json_use","w")
json.dump(citizens,file,indent=0)
file.close()