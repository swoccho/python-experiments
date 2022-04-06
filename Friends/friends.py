user_input = input("Enter 3 names of your friends using commas, (without space): ") .split(',')
people = open("people.txt", "r")
people_nearby = [line.strip() for line in people.readlines()]

people.close()


friends = set(user_input)
nearby_people = set(people_nearby)
nearby_friends = friends.intersection(nearby_people)


nearby_friends_file = open("nearby_friends.txt", "w")
for friend in nearby_friends:
    print(f"Hey! {friend} is nearby......Meet with him")
    nearby_friends_file.write(f"{friend}\n")
nearby_friends_file.close()