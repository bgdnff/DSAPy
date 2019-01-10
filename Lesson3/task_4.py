# 4. Определить, какое число в массиве встречается чаще всего.

import random
# ________генерация массива______________
SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# ________решение____________________

# 1.кажется, это можно было бы сделать с помощью словарей,
# но они на 5 уроке :) так что будем делать частотный словарь вручную...
# 2. Еще можно бы сделать вставку в словарь упорядоченной
# (по возрастанию/или убыванию), с бинарным поиском,
# но во-первых, не уверен что это не нарушает запрет на сортировку,
# а во-вторых - лениво :)

freq_dic = [[], []]
max_frequency = 0
max_frequency_number = 0
for item in array:
    for index,key in enumerate(freq_dic[0]):
        if key == item:
            freq_dic[1][index] += 1
            if freq_dic[1][index] > max_frequency:
                max_frequency = freq_dic[1][index]
                max_frequency_number = item
            break
    else:
        freq_dic[0].append(item)
        freq_dic[1].append(1)

print(f'чаще всего ({max_frequency} раз)встречается число {max_frequency_number}')
