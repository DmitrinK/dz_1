# ✔Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

user_num = None
from random import randint
num = randint(0, 1000)
count = 10
while count > 0:
    print("✔Программа загадывает число от 0 до 1000.")
    print(f"Колличество оставшихся попыток: {count} ")
    user_num = int(input("Введите угадываемое число: "))
    count -= 1
    if user_num == num:
        print(f"Вы угадали число с {10 - count} попытки")
        print("ПОЗДРАВЛЯЕМ!!!!!)))")
        break
    elif user_num < num:
        print("Введённое число меньше загаданного")
    elif user_num > num:
        print("Введённое число больше загаданного")
print("К сожалению вы не угадали((( Попробуйте ещё раз))")