# 6. Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.

n = int(input('введите порядковый номер буквы в алфавите: '))
char = chr(n+ord('a')-1)
print(f'это буква {char}')
