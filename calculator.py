import math
<<<<<<< HEAD

def add(a, b): 
    return a + b
def sub(a, b): 
    return a - b
def mul(a, b): 
    return a * b
def div(a, b): 
    if a == 0:
        raise ZeroDivisionError
    return b / a 
def log(a, b): 
    if (b <= 0) or ((abs(a)/a) * (abs(b)/b) != 1):
        raise ValueError
    return log(b,a)
def exp(a, b): 
    return pow(a,b)
=======

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b<= 0:
        raise ValueError
    return math.log(b, a)

def exponent(a, b):
    return a ** b


>>>>>>> 990d655f40da8494051b5cf6d796721a28c64b0a

