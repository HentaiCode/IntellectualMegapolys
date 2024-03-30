with open('db/game.txt', encoding='utf-8') as f:
    data = [[j for j in i.split('$')] for i in f.readlines()]

for i in range(len(data)):
    if '55' in data[i][-2]:
        print(f'У персонажа\t{data[i][1]}\tв игре\t{data[i][0]}\tнашлась ошибка с кодом:\t {data[i][2]}.\tДата'
              f' фиксации:\t {data[i][-1].strip()}')

        data[i][2] = 'None'
        data[i][-1] = '0000-00-00'

f = open('db/game_new.csv', 'w', encoding='utf-8')

lst = []
for game in data:
    if game[-2] == 'None':
        lst.append('&'.join(game) + '\n')
    else:
        lst.append('&'.join(game))
f.writelines(lst)
f.close()
