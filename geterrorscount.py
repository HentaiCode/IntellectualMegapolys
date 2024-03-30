with open('db/game.txt', encoding='utf-8') as f:
    data = [[j for j in i.split('$')] for i in f.readlines()]

errors = {}

for game in data:
    if game[0] not in errors:
        errors[game[0]] = 1
    else:
        errors[game[0]] += 1

for i in range(len(data)):
    data[i][-1] = data[i][-1].strip()
    data[i].append(str(errors[data[i][0]]) + '\n')

data.sort(key=lambda x: x[-1])

f = open('db/game_counter.csv', 'w', encoding='utf-8')

f.writelines(['$'.join(i) for i in data])
f.close()
