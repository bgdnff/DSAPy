# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
# равные части: в одной находятся элементы, которые не меньше медианы, в другой –
# не больше медианы. Задачу можно решить без сортировки исходного массива. Но если
# это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random


def generate_array(size):
    LOW = -100
    HIGTH = 100
    return [random.randint(LOW, HIGTH) for _ in range(size)]
    #return [86, -35, 7]


def median(array,q):
    pivot = random.choice(array)
    less = []
    more = []
    eq = []
    for item in array:
        if item > pivot:
            more.append(item)
        elif item < pivot:
            less.append(item)
        else:
            eq.append(pivot)

    if len(less) > q:
        return median(less, q)
    elif len(less) + len(eq) > q:
        return pivot
    else:
        return median(more, q - (len(less) + len(eq)))


size = int(input('введите размер массива(натуральный, нечетный)'))
array = generate_array(size)
print(array)
print('медиана:', median(array, size//2))
