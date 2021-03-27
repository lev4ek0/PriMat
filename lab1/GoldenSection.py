import math
import Const


def x1(a1, b1):
    return b1 - (math.sqrt(5) - 1) / 2 * (b1 - a1)


def x2(a1, b1):
    return a1 + (math.sqrt(5) - 1) / 2 * (b1 - a1)


def golden_section():
    A = Const.a
    B = Const.b
    counter1 = 0
    counter2 = 2
    X1 = x1(A, B)
    X2 = x2(A, B)
    Y1 = Const.f(X1)
    Y2 = Const.f(X2)
    while B - A > Const.e:
        counter1 += 1
        if X2 < X1:
            X1, X2 = X2, X1
            Y1, Y2 = Y2, Y1
        counter2 += 1
        if Y1 < Y2:
            B = X2
            X2 = x1(A, B)
            Y2 = Const.f(X2)
        elif Y1 > Y2:
            A = X1
            X1 = x2(A, B)
            Y1 = Const.f(X1)
        else:
            A = X1
            B = X2
            X1 = x1(A, B)
            X2 = x2(A, B)
            Y1 = Const.f(X1)
            Y2 = Const.f(X2)
    return {"Локальный минимум": (A + B) / 2, "Количество итераций": counter1, "Количество вычислений": counter2}
