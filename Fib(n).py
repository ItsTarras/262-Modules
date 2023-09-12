import math
from decimal import *
def fib(n):
    """Defines the nth fibonacci number in log(n) time, by using Binet's formula"""
    getcontext().prec = (1000000)
    print(Decimal(math.sqrt(5)))
    a = ((1 + Decimal(math.sqrt(5)))/2)**n
    b = ((1 - Decimal(math.sqrt(5)))/2)**n
    c = 1/Decimal(math.sqrt(5))
    fibonacci = ((a - b) * c)
    
    print(a)
    print(b)
    print(fibonacci)
    print(c)
fib(99)