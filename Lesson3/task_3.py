# 3. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

import random
# ________генерация массива______________
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# ________решение____________________

max_pos, min_pos = 0, 0
for index, item in enumerate(array):
    if item > array[max_pos]:
        max_pos = index
    elif item < array[min_pos]:
        min_pos = index
array[max_pos], array[min_pos] = array[min_pos], array[max_pos]

print(array)