with open('db/game.txt', encoding='utf-8') as f:
    data = [[j for j in i.split('$')] for i in f.readlines()]
    data.sort()


while (n := input('Введите имя персонажа: ')) != "game":
    count = 0
    print(f'Персонаж {n} встречается в играх:')
    for i in data:
        if i[1] == n:
            print('\t\t' + '+' + i[0])
            count += 1
        if count == 5:
            break
    print('________________________')
    print()