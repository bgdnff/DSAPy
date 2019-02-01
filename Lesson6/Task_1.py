import sys


def memory_count(func):
    def wrapper():
        def my_getsize(my_var):
            # позже была найдена готовая ф-ция рекурсивного подсчета памяти, занимаемой объектом,
            # но пусть уж остается как есть. идейно то же самое,
            # но там красивше и лучше с разными типами работает(например,
            # мой вариант может неверно посчитать словари)

            if id(my_var) in ids:  # если переменная с таким ИД уже была, то ее не считаем
                return 0

            ids[id(my_var)] = 1
            my_size = sys.getsizeof(my_var)
            if hasattr(my_var, "__iter__") and not isinstance(my_var, str):
                my_size += sum(my_getsize(spam) for spam in my_var)
            return my_size

        loc = func()
        ids = {}
        print(loc)
        memory = 0

        for var in loc:
            s = my_getsize(loc[var])
            print(f'{var} ->  {s}')
            memory += s
        return memory
    return wrapper


@memory_count
def test():
    var1 = 5
    var2 = 6
    var3 = [1, 2, 3]
    var33 = var3
    var4 = {1, 2}
    var5 = {"1": 2, "11": 3, '111': 4}
    var6 = 'qwerty'
    return locals()


@memory_count
def task2_8():
    # 8. Посчитать, сколько раз встречается определенная
    # цифра в введенной последовательности чисел.
    # Количество вводимых чисел и цифра, которую необходимо
    # посчитать, задаются вводом с клавиатуры.

    nombers_count = int(input('введите количество чисел: '))
    digit = int(input('введите искомую цифру: '))

    digit_count = 0
    for i in range(nombers_count):
        num = int(input(f'введите {i+1} число: '))
        while num > 0:
            if num % 10 == digit:
                digit_count += 1
            num //= 10
    print(f'во введенных числах цифра {digit} встречается {digit_count} раз')
    return locals()

@memory_count
def task3_9():
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
    return locals()


# print('функция потребляет памяти: ', test())
"""
{'var6': 'qwerty', 'var5': {'1': 2, '11': 3, '111': 4}, 'var4': {1, 2}, 'var33': [1, 2, 3], 'var3': [1, 2, 3], 'var2': 6, 'var1': 5}
var6 ->  31
var5 ->  217
var4 ->  144
var33 ->  62
var3 ->  0
var2 ->  14
var1 ->  14
функция потребляет памяти:  482
_________________________________________________________________
"""

#print('функция потребляет памяти: ', task2_8())
"""
{'num': 0, 'i': 4, 'digit_count': 5, 'digit': 5, 'nombers_count': 5}
num ->  12
i ->  14
digit_count ->  14
digit ->  0
nombers_count ->  0
функция потребляет памяти:  40
____________________________________________________________________
"""
print('функция потребляет памяти: ', task3_9())
"""
{'maximum': 22, 'j': 3, 'minimum': 17, 'i': 5, 'line': [21, 51, 25, 22, 8, 58], 'matrix': [[34, 3, 5, 86, 42, 78], [70, 25, 1, 26, 71, 17], [24, 56, 44, 42, 10, 72], [21, 51, 25, 22, 8, 58]], 'SIZE_Y': 4, 'random': <module 'random' from 'C:\\Users\\b\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\random.py'>, 'SIZE_X': 6, 'MIN_ITEM': 0, 'MAX_ITEM': 100}
maximum ->  14
j ->  14
minimum ->  14
i ->  14
line ->  138
matrix ->  438
SIZE_Y ->  14
random ->  44
SIZE_X ->  14
MIN_ITEM ->  12
MAX_ITEM ->  14
функция потребляет памяти:  730
__________________________________________________________
"""
# Примечания:
# 1. Обсчитываемая ф-ция должна быть декорирована @memory_count
#    и возвращать locals().
# 2. данный модуль считает все имена, в том числе вложенные функции
#    (без переменных в этих функциях, только заголовок) и
#     импортированые имена(напр. random).
# 3. подсчитывается ситуация (содержимое переменных)на конец выполнения
#    функции (вызов return) при этом в процессе выполнения могло быть
#    задействовано гораздо больше памяти

