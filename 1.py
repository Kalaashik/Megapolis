import csv

with open('game.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='$'))
    for row in reader:
        if '55' in row['nameError']:
            print(f'У персонажа {row["characters"]} в игре {row["GameName"]} нашлась ошибка с кодом: {row["nameError"]}. Дата фиксации: {row["date"]}')


with open('game_new.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['GameName', 'characters', 'nameError', 'date'],  delimiter='$')
    writer.writeheader()
    writer.writerows()