numbers = [4, 7, 2, 9, 5, 1, 6]
product = 1

for i in range(len(numbers)):
    if i % 2 != 0:
        product *= numbers[i]

print("Произведение элементов списка с нечетными номерами:", product)

maximum = max(numbers)
numbers.remove(maximum)
print("Новый список без наибольшего элемента:", numbers)