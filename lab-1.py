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
    if np.fabs(func(c)) < 0:
        return c

    if func(a) * func(c) < 0:
        return div_method(a, c, eps)
    if func(c) * func(b) < 0:
        return div_method(c, b, eps)

def main():
    ans = div_method(2, 10, 0.00001)
    print(ans) # print x

    #draw plow for testing
    x = np.arange(2.0, 10.0, 0.2)
    plt.plot(x, (x-2)**2 - 5)
    plt.axhline(0)
    plt.axvline(ans)
    plt.show()

if __name__ == "__main__":
    main()
