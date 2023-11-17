my_dict = {'a': 50, 'c': 5, 'd': 56, 'e': 4, 'f': 58, 'z': 20}

sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[0]))
first_three = list(sorted_dict.items())[:3]

print("Полученные первые три элемента:")
for key, value in first_three:
    print(key, ":", value)
