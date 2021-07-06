import json

json_list = []
csv_file = open('csv_file.txt', 'r')
lines = csv_file.readlines()
for line in lines[1:]:
    club, city, country = line.strip().split(',')
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)

csv_file.close()

json_file = open('json_file.txt', 'w')
convert= json.dump(json_list, json_file,indent=6)
json_file.close()

