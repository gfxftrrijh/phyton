#вариант 27
#задание 1

def countevenodddigits():
    number = input("Введите число: ")

    # Проверка на правильный ввод
    while not number.isdigit():
        number = input("Неправильный ввод. Введите число: ")

    evencount = 0
    oddcount = 0

    for digit in number:
        if int(digit) % 2 == 0:
            evencount += 1
        else:
            oddcount += 1

    return evencount, oddcount


even, odd = countevenodddigits()
print("Количество четных цифр:", even)
print("Количество нечетных цифр:", odd)