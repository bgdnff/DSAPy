# 9. Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

print('введите несколько натуральных чисел, 0 - конец ввода')
max_sum = 0
max_sum_number = 0

number = int(input('>'))
while number != 0:
    summa = 0
    tmp = number
    while tmp > 0:
        summa += tmp % 10
        tmp //= 10
    if summa > max_sum:
        max_sum = summa
        max_sum_number = number
    number = int(input('>'))
print(f'из введенных чисел наибольшую сумму цифр {max_sum} имеет число {max_sum_number}')
