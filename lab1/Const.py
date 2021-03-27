import math

a = 6.0
b = 9.0
e = 0.0000001


def f(x):
    return math.log(x * x, math.exp(1)) + 1 - math.sin(x)
