import math

a = 6
b = 9
e = 0.000001


def f(x):
    return math.log(x * x, math.exp(1)) + 1 - math.sin(x)
