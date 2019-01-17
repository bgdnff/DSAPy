# Определить, какое число в массиве встречается чаще всего.
import cProfile
import random



def generate_array(size):
    MIN_ITEM = 0
    return [random.randint(MIN_ITEM, size // 1.5) for _ in range(size)]
    # print(array)


# вариант 1
def var1(size):
    array = generate_array(size)
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]
    return num
#    if frequency > 1:
#        print(f'Число {num} встречется {frequency} раз(а)')
#    else:
#        print('Все элементы уникальны')
#cProfile.run('var1(2000)')
# 1    0.001    0.001    0.002    0.002 lesson3_task4.py:14(var1) - 100
# 1    0.000    0.000    0.001    0.001 lesson3_task4.py:7(generate_array) -100

# 1    0.034    0.034    0.038    0.038 lesson3_task4.py:14(var1) - 500
# 1    0.000    0.000    0.003    0.003 lesson3_task4.py:7(generate_array) - 500

# 1    0.158    0.158    0.166    0.166 lesson3_task4.py:14(var1) - 1000
# 1    0.000    0.000    0.007    0.007 lesson3_task4.py:7(generate_array) -1000

# 1    0.629    0.629    0.646    0.646 lesson3_task4.py:14(var1) - 2000
# 1    0.000    0.000    0.016    0.016 lesson3_task4.py:7(generate_array) - 2000

# 100 loops, best of 3: 1.99 msec per loop - 100
# 100 loops, best of 3: 36.2 msec per loop - 500
# 100 loops, best of 3: 139 msec per loop - 1000
# 100 loops, best of 3: 547 msec per loop - 2000

# похоже на О(n**2)

# ваниант 2____________________________________________
def var2(size):
    array = generate_array(size)
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] > frequency:
            frequency = counter[item]
            num = item
    return num
# if num is not None:
#    print(f'Число {num} встречется {frequency} раз(а)')
# else:
#    print('Все элементы уникальны')
#cProfile.run('var2(100000)')
# 1    0.000    0.000    0.001    0.001 lesson3_task4.py:45(var2) - 100
# 1    0.000    0.000    0.001    0.001 lesson3_task4.py:7(generate_array) - 100

# 1    0.000    0.000    0.004    0.004 lesson3_task4.py:45(var2) - 500
# 1    0.000    0.000    0.003    0.003 lesson3_task4.py:7(generate_array) - 500

# 1    0.001    0.001    0.008    0.008 lesson3_task4.py:45(var2) - 1000
# 1    0.000    0.000    0.007    0.007 lesson3_task4.py:7(generate_array) - 1000

# 1    0.001    0.001    0.017    0.017 lesson3_task4.py:45(var2) - 2000
# 1    0.000    0.000    0.016    0.016 lesson3_task4.py:7(generate_array) - 2000

# 1    0.097    0.097    1.128    1.128 lesson3_task4.py:45(var2) - 100000
# 1    0.000    0.000    1.031    1.031 lesson3_task4.py:7(generate_array) - 100000
# 100 loops, best of 3: 3.13 msec per loop - 500
# 100 loops, best of 3: 6.3 msec per loop - 1000
# 100 loops, best of 3: 12.8 msec per loop - 2000
# 100 loops, best of 3: 64.5 msec per loop - 10000
# 100 loops, best of 3: 727 msec per loop - 100000

# при увеличении размера массива время выполнения ф-ции увеличивается похоже линейно,
# составляя при этом менее 10% от времени генерации массива

# Мой вариант___________________________________________________________
def my_var(size):
    array = generate_array(size)
    freq_dic = [[], []]
    max_frequency = 1
    max_frequency_number = array[0]
    for item in array:
        for index, key in enumerate(freq_dic[0]):
            if key == item:
                freq_dic[1][index] += 1
                if freq_dic[1][index] > max_frequency:
                    max_frequency = freq_dic[1][index]
                    max_frequency_number = item
                break
        else:
            freq_dic[0].append(item)
            freq_dic[1].append(1)

    return max_frequency_number
    #print(f'чаще всего ({max_frequency} раз)встречается число {max_frequency_number}')
#cProfile.run('my_var(2000)')
# 1    0.000    0.000    0.001    0.001 lesson3_task4.py:7(generate_array) - 100
# 1    0.000    0.000    0.001    0.001 lesson3_task4.py:82(my_var) - 100

# 1    0.000    0.000    0.004    0.004 lesson3_task4.py:7(generate_array) - 500
# 1    0.010    0.010    0.013    0.013 lesson3_task4.py:82(my_var) - 500

# 1    0.000    0.000    0.007    0.007 lesson3_task4.py:7(generate_array) - 1000
# 1    0.043    0.043    0.050    0.050 lesson3_task4.py:82(my_var) - 1000

# 1    0.000    0.000    0.016    0.016 lesson3_task4.py:7(generate_array) - 2000
# 1    0.203    0.203    0.220    0.220 lesson3_task4.py:82(my_var) - 2000
# 100 loops, best of 3: 1.03 msec per loop - 100
# 100 loops, best of 3: 12.6 msec per loop - 500
# 100 loops, best of 3: 44.9 msec per loop - 1000
# 100 loops, best of 3: 180 msec per loop - 2000
# тоже похоже на О(n**2), но несколько быстрее чем var1
