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
        for d in range(2, int(n**0.5) + 1): ## SZ comment: range excludes its end, adding +1 will ensure n is included. # YT comment: Check divisors up to the square root of n.
# The +1 ensures the integer square root is included,
# since range() excludes its upper bound.
            if n % d == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes

def recaman(N:int):
    if not isinstance(N, int) or N < 1:
        raise ValueError("N must be an integer >= 1")
    recaman = [0, 1] #SZ comment: 0 is also part of the recaman
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
    #SZ comment: consider replacing the for loop with sorted function which reduces the complexity:
    common = sorted(set(list1) & set(list2)) # returns the sorted intersection of list1 and list2

    return common


def factor_pairs(n):
    factor_pairs = [
        (a, n // a)
        for a in range(1, int(n ** 0.5) + 1) #check the number till square root of n to prevent repetition
        if n % a == 0
    ]

    return factor_pairs

def random_walk(): # SZ comment: the random walk should not take in any parameters as number of steps to reach abs(10) is not fixed
    position = 0
    while abs(position) < 10:
        position += random.randint(0 , 1) * 2 - 1  #avoid 0
        yield position

list(random_walk()) # return the steps in a list

def random_walk(n): #SZ comment: as above
    position = 0
    walk = []
    while abs(position) < n:
        position += random.randint(0, 1) * 2 - 1
        walk.append(position)
        yield position
    return walk
