# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме
# последних элементов строк. Программа должна вычислять
# сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести
# полученную матрицу.

SIZE_Y = 5
SIZE_X = 4
matrix = []
for j in range(SIZE_Y):
    line = []
    summa = 0
    for i in range(SIZE_X - 1):
        item = int(input(f'введите {i} элемент {j} строки:'))
        summa += item
        line.append(item)
    line.append(summa)
    matrix.append(line)

for line in matrix:
    print(line)