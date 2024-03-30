def alphagetsort(mass):
    letters = 'ABCDEFGHKLOMNOPQRSTUVWXYZ'


with open('db/game.txt', encoding='utf-8') as f:
    data = [[j for j in i.split('$')] for i in f.readlines()]


