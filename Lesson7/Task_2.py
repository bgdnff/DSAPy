# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50). Выведите на
# экран исходный и отсортированный массивы.
import random


def generate_array(size):
    LOW = 0
    HIGTH = 50
    return [random.random()*(HIGTH-LOW)+LOW for _ in range(size)]

def merge_sort(array, left, right):

    if left == right:
        return array[left:left+1]

    result = []
    middle = int((left + right)/2)
    # сортировка половинок
    left_array = merge_sort(array, left, middle)
    right_array = merge_sort(array, middle+1, right)

    # слияние
    left_idx = 0
    right_idx = 0
    while left_idx < len(left_array) and right_idx < len(right_array):
        if left_array[left_idx] > right_array[right_idx]:
            result.append(right_array[right_idx])
            right_idx += 1
        else:
            result.append(left_array[left_idx])
            left_idx += 1
    if left_idx < len(left_array):
        result += left_array[left_idx:len(left_array)]
    else:
        result += right_array[right_idx:len(left_array)]
    return result


array = generate_array(25)
print(array)
print(merge_sort(array, 0, len(array)))
