from collections import defaultdict
import copy

with open("polimer.txt") as change:
    # разделяем фал по строкам и избавляемся от ненужных символов
    raw_polimer = change.read().split("\n")

# избавляемся от ненужных символов
template = raw_polimer[0]
rules = [line.split(" -> ") for line in raw_polimer[2:]]
#создаем словарь со значениями по умолчанию
header = defaultdict(int)
# тут откидываем последний элемент, которому нету пары
for i in range(len(template) - 1):
    # считаем
    header[template[i:i + 2]] += 1

# суть функции такова: удалить из нового словаря старый, добвать новые значения и с их учетом, добавить к новому славорю новый.
def new_line_project(header):
    # копирует словарь
    new_header = copy.copy(header)
    for pair in header:
        for start, end in rules:
            if pair == start:
                # из нового словаря отнимаем старый, зетм всем обнулившимся элементам доболяем окночания (т.е. всем новым) и возращаем старые значения тем элементам, которые остались.
                new_header[pair] -= header[pair]
                new_header[pair[0] + end] += header[pair]
                new_header[end + pair[1]] += header[pair]
                break

    return new_header

# перебираем последовательности
for i in range(40):
    header = new_line_project(header)
print(header)
count = defaultdict(int)
# берем только первый символ и смотрим сколько раз он встретился. (можно взять и два символа count[pair[1]] += header[pair]. Тогда i[1] //2)
for pair in header:
    count[pair[0]] += header[pair]

counts = [i[1] for i in count.items()]

print('Максимальное значение: ', max(counts))
print('Минимальное значение: ', min(counts))
print('Разница значений: ', (max(counts) - min(counts)))