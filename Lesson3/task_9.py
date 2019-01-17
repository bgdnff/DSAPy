# 9. Найти максимальный элемент среди
# минимальных элементов столбцов матрицы.

####### генерация матрицы
import random

SIZE_X = 6
SIZE_Y = 4

MIN_ITEM = 0
MAX_ITEM = 100

matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_X)] for _ in range(SIZE_Y)]
for line in matrix:
    print(line)

###### решение

# если бы требовалось найти макс из мин по строкам, то все было бы просто,
# просматриваем построчно, ищем минимумы и максимум, однако, нам нужны столбцы,
# поэтому будем использовать обращение к элементам матрицы по индексам,
# что как я понял, не комильфо для python, но что делать...
# кстати, цикл с обращением по индексу действительно
# работает хуже чем при работе с матрицей как со списками,
# или это только эстетическое пожелание?


for i in range(SIZE_X):
    minimum = matrix[0][i]
    for j in range(SIZE_Y):
        if minimum > matrix[j][i]:
            minimum = matrix[j][i]
    if i == 0 or maximum < minimum:
        maximum = minimum

print(f'максимальный минимум по столбцам: {maximum}')