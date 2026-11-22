# https://github.com/elliottscarlett-ufl/lab11-ES-EM.git
# Partner 1: Elliott Scarlett
# Partner 2: Elijah Morgan


import math


def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b): 
    return a ** b

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError:
        raise ValueError

def hypotenuse(a, b):
    return math.hypot(a, b)