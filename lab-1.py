from __future__ import division

import matplotlib.pyplot as plt
import numpy as np


# f(x) = (x-2)**2 - 5, [a,b] = [2,10]
def func(x):
    return (x-2)**2 - 5

def div_method(a, b, eps):
    c = (a + b) / 2

    if b - a < eps:
        return c
    if np.fabs(func(c)) - eps  < 0:
        return c

    if func(a) * func(c) < 0:
        return div_method(a, c, eps)
    if func(c) * func(b) < 0:
        return div_method(c, b, eps)

def d_fun(x):
    st = 1e-5
    return (func(x+st)-func(x)) / st

def newton_method(a, b, eps):
    try:
        if func(a) * func(b) > 0:
            raise RuntimeError("Bad a or b")

        if func(a) * d_fun(d_fun(a)) < 0:
            x0 = a
        else:
            x0 = b

        xn = x0 - func(x0) / d_fun(x0)
        while np.fabs(x0 - xn) > eps:
            x0 = xn
            xn = x0 - func(x0) / d_fun(x0)

        return xn

    except RuntimeError:
        raise


def relax_method(a, b, eps):
    m, M = d_fun(a), d_fun(b)
    if m > M:
        m, M = M, m
    tau = 2 / (m + M)
    if d_fun(a) > 0:
        tau *= -1
    prev_x = a
    while True:
        x = prev_x + tau * func(prev_x)
        if np.fabs(x - prev_x) <= eps:
            return x
        prev_x = x

def main():
    #ans = div_method(2, 10, 0.00001)
    #ans = newton_method(2, 10, 0.00001)
    ans = relax_method(2, 10, 0.00001)
    print(ans) # print x

    #draw plot for testing
    x = np.arange(2.0, 10.0, 0.2)
    plt.plot(x, (x-2)**2 - 5)
    plt.axhline(0)
    plt.axvline(ans)
    plt.show()

if __name__ == "__main__":
    main()
