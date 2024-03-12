import csv

with open('game.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='$'))
    pers = input()
    games = []  # список с играми
    k = 0  # счетчик
    flag = 0  # флаг
    for row in reader:  # не смогла сделать неогранниченный ввод, поэтому чтобы снова ведстиперсонажа, нужно перезапускать код
        flag = 0
        if pers in row['characters']:
            k += 1
            games.append(row['GameName'])
            if k == 5:
                print(f'Персонаж {row["characters"]} встречается в играх:')
                for i in games:
                    print(i)
                k = 0
                game = []
                flag = 1
                break

    if k != 0 and flag == 0:
        print(f'Персонаж {row["characters"]} встречается в играх:')
        for i in games:
            print(i)
        k = 0
        game = []
    elif k == 0 and flag == 0:
        print('Этого персонажа не существует')

