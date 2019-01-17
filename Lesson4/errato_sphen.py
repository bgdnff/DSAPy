
# Простые числа считаем по-человечески, т.е.
# 2 - это первое простое число, 3 - второе и т.д.
# нулевого простого числа нет.

import math
import  cProfile


def get_size(count):
    return int(count*math.log2(count)) if count > 4 else 10


def sieve(count):
    size = get_size(count)
    _sieve = [i for i in range(size)]
    _sieve[1] = 0
    primes_counter = 0
    for i in range(2, size):
        if _sieve[i] != 0:
            j = i + i
            primes_counter += 1
            if primes_counter == count:
                return i
            while j < size:
                _sieve[j] = 0
                j += i


def non_sieve(count):
    primes = [2]
    current = 3
    while len(primes) < count:
        for pr in primes:
            if current % pr == 0:
                break
        else:
            primes.append(current)
        current += 1
    return primes[len(primes)-1]
#print(sieve(1))
cProfile.run('sieve(1000)')
# 1    0.010    0.010    0.011    0.011 errato_sphen.py:14(sieve) - 1000
# 1    0.023    0.023    0.026    0.026 errato_sphen.py:14(sieve) - 2000
# 1    0.046    0.046    0.051    0.051 errato_sphen.py:14(sieve) - 4000
# 1    0.067    0.067    0.073    0.073 errato_sphen.py:14(sieve) - 5000
# 1    0.137    0.137    0.155    0.155 errato_sphen.py:14(sieve) - 10000
#print(non_sieve(1))
#cProfile.run('non_sieve(4000)')
# 1    0.100    0.100    0.102    0.102 errato_sphen.py:32(non_sieve) - 1000
# 1    0.425    0.425    0.430    0.430 errato_sphen.py:32(non_sieve) - 2000
# 1    1.872    1.872    1.885    1.885 errato_sphen.py:32(non_sieve) - 4000
# 1    3.269    3.269    3.282    3.282 errato_sphen.py:32(non_sieve) - 5000
# 1   15.924   15.924   15.953   15.953 errato_sphen.py:32(non_sieve) - 10000
