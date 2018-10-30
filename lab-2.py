from __future__ import division
from __future__ import print_function

import numpy as np

def gen_matrix(n, x, a):
    b = [0] * n
    for i in range(n):
        for j in range(n):
            b[i] += a[i][j] * x[j]
    return b

def gause_method(n, a, b):
    for i in range(0, n-1):
        for j in range(i+1, n):
            kof = a[j][i] / a[i][i]
            for k in range(i, n + 1):
                if k == n:
                    b[j] -= b[i] * kof
                else:
                    a[j][k] -= a[i][k] * kof
    x = [0] * n
    for i in range(n - 1, -1, -1 ):
        for j in range(n -1, i -1, -1):
            if i == j:
                x[i] = b[i] / a[i][j]
            else:
                b[i] -= a[i][j] * x[j]
    return x
def check_ans(x, ans, eps):
    for i in range(len(x)):
        if np.fabs(x[i] - ans[i]) > eps:
            return False
    return True
def main():
    n = int(input("Enter n : "))
    eps = 1e-5
    x, a = np.random.rand(n), np.random.rand(n, n)
    b = gen_matrix(n, x, a)
    xans = gause_method(n, a, b)
    print (x, '\n', xans)
    print(check_ans(x, xans, eps))
if __name__ == "__main__":
    main()