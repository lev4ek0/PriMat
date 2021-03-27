import Const


def parabol(x1, x2, x3):
    f1 = Const.f(x1)
    f2 = Const.f(x2)
    f3 = Const.f(x3)
    return x2 - (pow((x2 - x1), 2) * (f2 - f3) - pow((x2 - x3), 2) * (f2 - f1)) / (2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1)))


def parabola():
    X1 = Const.a
    X3 = Const.b
    counter1 = 0
    counter2 = 0
    while X3 - X1 > Const.e / 2:
        counter1 += 1
        X2 = (X1 + X3) / 2
        U = parabol(X1, X2, X3)
        counter2 += 3
        if U < X2:
            U, X2 = X2, U
        Y1 = Const.f(X2)
        Y2 = Const.f(U)
        counter2 += 2
        if Y1 < Y2:
            X3 = U
        elif Y1 > Y2:
            X1 = X2
        else:
            X1 = X2
            X3 = U
    return {"Локальный минимум": (X1 + X3) / 2, "Количество итераций": counter1, "Количество вычислений": counter2}
