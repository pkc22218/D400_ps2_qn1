import math
import random

def sin(x):
    sin_x = 0.0
    for n in range(0, 3):  # n = 2 is the x^5 term, n=3 not included
        sin_x += ((-1) ** n) * x ** (2 * n + 1) / math.factorial(2 * n + 1)
    return f'The value of sin({x}) using its Taylor expansion to order of 5 is {sin_x:.5f}.'# print the wording and formatting to the 5 decimal.

def primes(N:int):
    if not isinstance(N, int) or N < 1:
        raise ValueError("N must be an integer >= 1")
    primes = []
    for n in range(2, N):
        is_prime = True
        for d in range(2, n):
            if n % d == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes

def recaman(N:int):
    if not isinstance(N, int) or N < 1:
        raise ValueError("N must be an integer >= 1")
    recaman = [1]
    for n in range (2, N + 1):
        previous = recaman[-1]
        if previous > n and previous - n not in recaman:
            recaman.append(previous - n)
        else:
            recaman.append(previous + n)
    return recaman 

def common_number(N:int): # create a list of the numbers which appear in both prime and recaman when they are both N items long.
    if not isinstance(N, int) or N < 1:
        raise ValueError("N must be an integer >= 1")
    
    limit = 2
    list1 = primes(limit)

    while len(list1) < N:
        limit *= 2
        list1 = primes(limit)

    list1 = list1[:N]
    list2 = recaman(N)

    common = []
  
    for number in list1:
        if number in list2 and number not in common:
            common.append(number)

    return common


def factor_pairs(n):
    factor_pairs = [
        (a, n // a)
        for a in range(1, int(n ** 0.5) + 1) #check the number till square root of n to prevent repetition
        if n % a == 0
    ]

    return factor_pairs

def random_walk(n): 
    steps = []
    position = 0
    while abs(position) < 10:
        position += random.randint(0 , 1) * 2 - 1  #avoid 0
        for n in range (1, n + 1):
            walk = [sum(steps[:i+1]) for i in range(n)]
    yield walk

def random_walk(n):
    position = 0
    walk = []
    while abs(position) < n:
        position += random.randint(0, 1) * 2 - 1
        walk.append(position)
        yield position
    return walk