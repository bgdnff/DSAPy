#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


nnn = int(input("Введите целое положительное трехзачное число"))
n1 = nnn % 10
nnn //= 10
n2 = nnn % 10
n3 = nnn // 10
sum3 = n1+n2+n3
mult3 = n1*n2*n3
print(f'сумма цифр = {sum3}')
print(f'произведение цифр = {mult3}')
