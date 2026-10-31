import math
from re import L

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
    for n in range (2,N):
        previous = recaman[-1]
        if previous > n and previous - n not in recaman:
            recaman.append(previous - n)
        else:
            recaman.append(previous + n)
    return recaman 

def common_number(N:int):
    common = []
    list1 = primes(N)
    list2 = recaman(N)
    for number in list1:
        if number in list2 and number not in common:
            common.append(number)

    return common


