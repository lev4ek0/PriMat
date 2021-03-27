import math
import Const
import Parabola
import numpy


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
        flag = 0
        if x != w and w != v and x != v and Yx != Yw and Yw != Yv and Yx != Yv:
            u = Parabola.parabol(x, w, v)
            counter2 += 3
            if A + Const.e < u < B - Const.e and abs(u - x) < g / 2:
                d = abs(u - x)
                flag = 1
        if flag == 0:
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
    return [(A + B) / 2, counter1, counter2]
