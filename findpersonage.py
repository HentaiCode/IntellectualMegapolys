# Открытие и сортировка базы данных в переменную data
with open('db/game.txt', encoding='utf-8') as f:
    data = [[j for j in i.split('$')] for i in f.readlines()]
    data.sort()

# С помощью ктулху оператора осущствлен динамический ввод данных
while (n := input('Введите имя персонажа: ')) != "game":
    count = 0
    print(f'Персонаж {n} встречается в играх:')
    # Нахождение нужного персонажа
    for i in data:
        if i[1] == n:
            print(i[0])
            count += 1
        if count == 5:
            break