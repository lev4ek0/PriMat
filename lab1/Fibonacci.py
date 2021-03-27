import math
import Const


def F(n):
    return 1 / math.sqrt(5) * (pow((1 + math.sqrt(5)) / 2, n) - pow((1 - math.sqrt(5)) / 2, n))


def fibonacci():
    n = 0
    while ((Const.b - Const.a) / Const.e) > F(n + 2):
        n += 1
    X1 = Const.a + F(n) / F(n + 2) * (Const.b - Const.a)
    X2 = Const.a + F(n + 1) / F(n + 2) * (Const.b - Const.a)
    Y1 = Const.f(X1)
    Y2 = Const.f(X2)
    k = 1
    A = Const.a
    B = Const.b
    counter1 = 0
    counter2 = 0
    while True:
        counter1 += 1
        if Const.f(X1) > Const.f(X2):
            counter2 += 2
            A = X1
            X1 = X2
            X2 = A + F(n - k - 1) / F(n - k) * (B - A)
            if k == n - 2:
                break
            else:
                k += 1
        else:
            counter2 += 2
            B = X2
            X2 = X1
            X1 = A + F(n - k - 2) / F(n - k) * (B - A)
            if k == n - 2:
                break
            else:
                k += 1
    X2 = X1 + Const.e
    if Y1 >= Y2:
        A = X1
    else:
        B = X2
    return {"Локальный минимум": (A + B) / 2, "Количество итераций": counter1, "Количество вычислений": counter2}
