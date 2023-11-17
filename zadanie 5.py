toys = {
    "Машинка": ["Красная машинка", 500, 10],
    "Кукла": ["Кукла Барби", 700, 5],
    "Пазл": ["Пазл с изображением зверей", 300, 7],
    "Мяч": ["Футбольный мяч", 1000, 3],
    "Конструктор": ["Конструктор Lego", 1500, 2],
    "Кубик-Рубик": ["Головоломка", 600, 4]
}

def show_description():
    print("Описания игрушек:")
    for toy, details in toys.items():
        print(toy, "-", details[0])

def show_prices():
    print("Цены игрушек:")
    for toy, details in toys.items():
        print(toy, "-", details[1])

def show_quantities():
    print("Количество игрушек:")
    for toy, details in toys.items():
        print(toy, "-", details[2])

def show_all_info():
    print("Информация об игрушках:")
    for toy, details in toys.items():
        print("Игрушка:", toy)
        print("Описание:", details[0])
        print("Цена:", details[1])
        print("Количество:", details[2])
        print("--------------------")

def buy_toy():
    total_price = 0
    while True:
        toy_name = input("Введите название игрушки (или 'n' для выхода): ")
        if toy_name == "n":
            break
        if toy_name not in toys:
            print("Такой игрушки нет в магазине.")
            continue
        quantity = int(input("Введите количество: "))

        if quantity > toys[toy_name][2]:
            print("Недостаточное количество в магазине.")
            continue

        price = toys[toy_name][1]
        total_price += price * quantity
        toys[toy_name][2] -= quantity

    print("Суммарная стоимость покупки:", total_price)
    print("Остаток игрушек в магазине:")
    show_quantities()

while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    choice = input("Выберите пункт меню (или 'q' для выхода): ")

    if choice == "1":
        show_description()
    elif choice == "2":
        show_prices()
    elif choice == "3":
        show_quantities()
    elif choice == "4":
        show_all_info()
    elif choice == "5":
        buy_toy()
    elif choice == "q":
        break
    else:
        print("Неправильный выбор. Попробуйте снова.")