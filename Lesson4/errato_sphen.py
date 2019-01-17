import math
import  cProfile


def get_size(count):
    return int(count*math.log2(count)) if count > 4 else 10


def sieve(count):
    size = get_size(count)
    _sieve = [i for i in range(size)]
    print(_sieve)
    _sieve[1] = 0
    primes_counter = 0
    for i in range(2, size):
        if _sieve[i] != 0:
            j = i + i
            primes_counter += 1
            #print(i,primes_counter)
            if primes_counter == count:
                return i
            while j < size:
                _sieve[j] = 0
                j += i


def non_sieve(count):
    primes = [2]
    if count < 2:
        return False
    prime = True
    current = 3
    while len(primes) < count:
        pass

print(sieve(100))
