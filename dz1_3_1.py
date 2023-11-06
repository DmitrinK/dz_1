user_answer = "нет"
max_limit = 1000
min_limit = 0
comp = None
count = 1
while user_answer != "+":
    from random import randint
    user_num = randint(min_limit, max_limit)
    print(f"Попытка номер: {count}")
    user_answer = input(f"Ваше число: {user_num}?  +/-: ")
    if user_answer == "+":
        print("Рад был угадать))")
        break
    comp = input("Ваше число больше или меньше (б/м) ?:   ")
    if comp == "б":
        min_limit = user_num
    else:
        max_limit = user_num
    count += 1
print("до новых встреч")