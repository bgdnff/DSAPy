# 7. В одномерном массиве целых чисел определить два
# наименьших элемента. Они могут быть как равны между
# собой (оба являться минимальными), так и различаться.
import random
# генерация массива
SIZE = 20 # должно быть >=2   !!! ;-)
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# решение
double_min = [MAX_ITEM, MAX_ITEM]
for item in array:
    if item < double_min[0]:
        double_min[0] = item
        if double_min[0] < double_min[1]:  # надеюсь, это не считается запрещенной сортировкой?
            double_min[0], double_min[1] = double_min[1], double_min[0]

print(f'минимальные значения в массиве: {double_min[0]}, {double_min[1]}')
