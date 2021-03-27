import Const


def x1(a1, b1):
    return (a1 + b1) / 2 - Const.e / 2


def x2(a1, b1):
    return (a1 + b1) / 2 + Const.e / 2


def dichotomy():
    A = Const.a
    B = Const.b
    counter1 = 0
    counter2 = 0
    while B - A > Const.e:
        X1 = x1(A, B)
        X2 = x2(A, B)
        counter1 += 1
        Y1 = Const.f(X1)
        Y2 = Const.f(X2)
        counter2 += 2
        if Y1 < Y2:
            B = X2
        elif Y1 > Y2:
            A = X1
        else:
            A = X1
            B = X2
    return {"Локальный минимум": (A + B) / 2, "Количество итераций": counter1, "Количество вычислений": counter2}
