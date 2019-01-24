# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это
# цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
# [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

HEX = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def get_last_digit(num):
# из списка с HEX цифрами возвращает значение последней цифры(int),
# из пустого списка возвращает 0
    if len(num) > 0:
        return HEX.index(num.pop())
    else:
        return 0


def hex_sum(a: list, b: list):
    # дублируем списки, чтобы не портились
    a = a[::]
    b = b.copy()
    summa = deque()
    over = 0
    while len(a) > 0 or len(b) > 0:
        digit_sum = over + get_last_digit(a) + get_last_digit(b)
        if digit_sum > 15:
            over = 1
            digit_sum -= 16
        else:
            over = 0
        summa.appendleft(HEX[digit_sum])
    if over > 0:
        summa.appendleft(HEX[over])
    return list(summa)


def hex_mult(a, b):
    result = []
    for digit_a in a:
        int_a = HEX.index(digit_a)
        line = deque()
        over = 0
        for digit_b in reversed(b):
            digit_mul = int_a * HEX.index(digit_b) + over
            over = digit_mul // 16
            digit_mul %= 16
            line.appendleft(HEX[digit_mul])
        if over > 0:
            line.appendleft(HEX[over])
        if result != ['0']:   # чтобы не получился список из нескольких нулей
            result.append('0')
        result = hex_sum(result, line)
    return result


first = list(str.upper(input('введите первое HEX число:')))
second = list(str.upper(input('введите второе HEX число:')))

print(f'сумма : {"".join(hex_sum(first, second))}')
print(f'произведение : {"".join(hex_mult(first, second))}')

