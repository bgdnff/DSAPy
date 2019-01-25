# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю
# прибыль (за год для всех предприятий) и вывести наименования
# предприятий, чья прибыль выше среднего и отдельно вывести
# наименования предприятий, чья прибыль ниже среднего.
from collections import namedtuple, Counter

n = int(input('введите количество предприятий:'))
if n < 1:
    print('должно быть >0!')
    exit(0)
Enterprize = namedtuple('Enterprize', 'name, profit')
base = []
average = Counter(profit=0)
for spam in range(n):
    _name = input(f'введите название предприятия {n+1}: ')
    _profit = Counter(profit=0)
    for eggs in range(4):
        _profit += Counter(profit=float(input(f'введите прибыль за {eggs+1} квартал:')))
    base.append(Enterprize(_name, Counter(_profit)))
    average += _profit
print(base)
average['profit'] = average['profit']/n
print(average)
less = []
more = []
for ent in base:
    if ent.profit['profit'] > average['profit']:
        more.append(ent.name)
    elif ent.profit['profit'] < average['profit']:
        less.append(ent.name)

print('прибыль выше среднего у предприятий:')
print(more)
for e in more:
    print(e)
print('прибыль ниже среднего у предприятий:')
for e in less:
    print(e)
