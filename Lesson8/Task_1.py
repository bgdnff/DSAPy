# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
import hashlib

# Саму строку тоже считаем своей собственной подстрокой.
def count_substrings(str):
    subs = set()
    for i in range(0,len(str)):
        for j in range(i+1,len(str)+1):
            sub = str[i:j]
            sub_hash = hashlib.sha1(sub.encode('utf-8')).hexdigest()
            if sub_hash not in subs:
                subs.add(sub_hash)
    return len(subs)


str = input('введите строку:')
print(f'неповторяющихся подстрок :{count_substrings(str)}')


