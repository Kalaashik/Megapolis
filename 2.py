import csv
import random


def quicksort(n):  # функция быстрой сортировки
    if len(n) <= 1:
        return n
    else:
        l_list = []
        m_list = []
        r_list = []
        q = random.choice([x for x in n])
        for a in n:
            if a['GameName'] < q['GameName']:
                l_list.append(a)
            elif a['GameName'] > q['GameName']:
                r_list.append(a)
            else:
                m_list.append(a)
        return quicksort(l_list) + m_list + quicksort(r_list)


with open('game.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='$'))
    reader = quicksort(reader)  # сортировка по названию игры












