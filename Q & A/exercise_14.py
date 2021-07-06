question_open = open("question.txt", "r")

question_list= [line.strip() for line in question_open]

question_open.close()

score = 0
total = len(question_list)


for line in question_list:
    q, a = line.split("=")

    user_input = input(f"{q} = ")
    if a == user_input:
        score += 1

result_open = open("result.txt" , "w")
result_open.write(f"Your final score is {score} / {total}")
result_open.close()
