def hash(s):
    p = 65
    m = 10**9 + 9
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters += letters.upper()
    letters += '1234567890:-'

    hs = 0

    for i in range(len(s)):
        hs += (letters.index(s[0]) + 1) * (p ** i)

    return hs % m


if __name__ == '__main__':
    with open('db/game.txt', encoding='utf-8') as f:
        data = [[j for j in i.split('$')] for i in f.readlines()]

    for i in range(len(data)):
        data[i] = [str(hash(''.join(data[i][:2]).replace(' ', '')))] + data[i]

    f = open('db/game_with_hash.csv', 'w', encoding='utf-8')

    f.writelines(['$'.join(i) for i in data])
    f.close()

