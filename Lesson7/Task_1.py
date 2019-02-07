# 1. Отсортируйте по убыванию методом "пузырька" одномерный
# целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный
# массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
import random


def generate_array(SIZE):
    LOW = -100
    HIGTH = 100
    return [random.randint(LOW, HIGTH-1) for _ in range(SIZE)]


def bubble_sort(array):
    for n in range(1, len(array)):
        no_changes = True
        for i in range(0, len(array)-n):
            # до конца идти не нужно, там собирается отсортированный массив
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                no_changes = False
        print(array)
        if no_changes:
            # если не произошло ни одного обмена, значит уже отсортировали, дальше продолжать не нужно
            break
    return array
array = generate_array(30)
print(array)
print(bubble_sort(array))
