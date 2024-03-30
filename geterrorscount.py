def geterrcount(games):
    '''

    :param games: Весь массив игр
    :return: Хеш-таблицу вида "игра: кол-во ошибок"
    '''
    errs = {}

    for game in games:
        if game[0] not in errs:
            errs[game[0]] = 1
        else:
            errs[game[0]] += 1

    return errs


if __name__ == '__main__':
    with open('db/game.txt', encoding='utf-8') as f:
        data = [[j for j in i.split('$')] for i in f.readlines()]

    errors = geterrcount(data)

    # Запись в файл
    data[0].append('counter\n')
    data[0][-2] = data[0][-2].strip()

    for i in range(1, len(data)):
        data[i][-1] = data[i][-1].strip()
        data[i].append(str(errors[data[i][0]]) + '\n')

    d1 = [data[0]] + sorted(data[1:], key=lambda x: x[-1])

    f = open('db/game_counter.csv', 'w', encoding='utf-8')

    f.writelines(['$'.join(i) for i in d1])
    f.close()

    # Вывод для второй задачи
    for i in errors:
        print(f'{i} - количество багов: {errors[i]}')
