import string
with open("polimer.txt") as change:
    # разделяем фал по строкам и избавляемся от ненужных символов
    raw_polimer = change.read().split("\n")

# избавляемся от ненужных символов
template = raw_polimer[0]
rules = [line.split(" -> ") for line in raw_polimer[2:]]

# суть функции такова: взять последовательность, добваить в неё новые значения в нужном порядке и создать новую последовательность на месте старой.
def new_line_project(s):
    new_str = ""
    i = 0
    while i < len(s):
        new_str += s[i]
        for start, end in rules:
            # берем нужyst нужные элементы
            if s[i:i + 2] == start:
                # дополyяем конечным значением
                new_str += end
                break
        i += 1

    return new_str
# перечисляем весь англиский алфовит в вверхнем регистре
elements = string.ascii_uppercase
# перебираем последовательности
for i in range(20):
    template = new_line_project(template)
# перебераем весь англиский алфовит и считаем кол-во букв
counts = [template.count(j) for j in elements if template.count(j)]
print('Максимальное значение: ',max(counts))
print('Минимальное значение: ',min(counts))
print('Разница значений: ',(max(counts) - min(counts)))
print(template)
