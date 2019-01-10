# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
# ________генерация массива______________
SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# ________решение____________________

max_pos = -1
maximum = MIN_ITEM
for index, item in enumerate(array):
    if 0 > item > maximum:
        max_pos = index
        maximum = item

if max_pos > -1:
    print(f'максимальный отрицатльный элемент массива : {maximum}')
    print(f'расположен в позиции : {max_pos}')
else:
    print('в массиве нет отрицательных элементов')