import math
import Const
import numpy


def parabol(x1, x2, x3, f1, f2, f3):
    if x1 > x2:
        x1, x2 = x2, x1
        f1, f2 = f2, f1
    if x2 > x3:
        x2, x3 = x3, x2
        f2, f3 = f3, f2
    if x1 > x3:
        x1, x3 = x3, x1
        f1, f3 = f3, f1
    return x2 - (pow((x2 - x1), 2) * (f2 - f3) - pow((x2 - x3), 2) * (f2 - f1)) / (2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1)))


def brent():
    K = (3 - math.sqrt(5)) / 2
    x = w = v = u = (Const.a + Const.b) / 2
    Yx = Yw = Yv = Const.f(x)
    d = e = Const.b - Const.a
    A = Const.a
    B = Const.b
    counter1 = 0
    counter2 = 1
    while abs(B - A) > Const.e * 2:
        counter1 += 1
        g = e
        e = d
        if x != w and w != v and x != v and Yx != Yw and Yw != Yv and Yx != Yv:
            u = parabol(x, w, v, Yx, Yw, Yv)
            if A + Const.e < u < B - Const.e and abs(u - x) < g / 2:
                d = abs(u - x)
        else:
            if x < (B - A) / 2:
                u = x + K * (B - x)
                d = B - x
            else:
                u = x - K * (x - A)
                d = x - A
            if abs(u - x) < Const.e:
                u = x + numpy.sign(u - x) * Const.e
        Yu = Const.f(u)
        counter2 += 1
        if Yu <= Yx:
            if u >= x:
                A = x
            else:
                B = x
            v = w
            w = x
            x = u
            Yv = Yw
            Yw = Yx
            Yx = Yu
        else:
            if u >= x:
                B = u
            else:
                A = u
            if Yu <= Yv or w == x:
                v = w
                w = u
                Yv = Yw
                Yw = Yu
            elif Yu <= Yw or v == x or v == w:
                v = u
                Yv = Yu
    return {"Локальный минимум": (A + B) / 2, "Количество итераций": counter1, "Количество вычислений": counter2}
