#✔Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется
# больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = None
b = None
c = None

while 1 > 0:
    a, b, c = int(input("Введите a: ")), int(input("Введите b: ")), int(input("Введите c: "))
    print(a, b, c)
    if a > b+c or b > a+c or c > a+b:
        print("треугольника с такими сторонами не существует")
    elif a == b == c:
        print("треугольник является равносторонним")
    elif a == b or a == c or b == c:
        print("треугольник является равнобедренным")
    else:
        print("треугольник является разносторонним")
