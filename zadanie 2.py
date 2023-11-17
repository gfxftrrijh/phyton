# вариант 27
# задание 2

def countupperlowerpairs():
    word = input("Введите слово: ")

    # Проверка на правильный ввод
    while not word.isalpha():
        word = input("Неправильный ввод. Введите слово: ")

    upperpairs = 0
    lowerpairs = 0
    totalletters = len(word)

    for i in range(len(word) - 1):
        if word[i].isupper() and word[i + 1].isupper():
            upperpairs += 1
        if word[i].islower() and word[i+1].islower():
            lowerpairs += 1

    return upperpairs, lowerpairs, totalletters


upper, lower, total = countupperlowerpairs()
print("Количество пар верхнего регистра:", upper)
print("Количество пар нижнего регистра:", lower)
print("Всего букв в слове:", total)
