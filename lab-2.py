import numpy as np

def gen_matrix(n, x, a):
    b = np.zeros(n)
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

def yakobi_method(n, a, b, eps):
    x0 = np.zeros(n)
    xn = np.zeros(n)
    B = np.zeros((n,n))
    d = np.zeros(n)

    for i in range(n):
        for j in range(n):
            if j == i:
                B[i][i] = 0
            else:
                B[i][j] = (-a[i][j] / a[i][i])
        d[i] = b[i] / a[i][i]

    e1 = (1 - np.linalg.norm(B, np.inf)) / np.linalg.norm(B, np.inf) * eps

    x0 = d
    xn = np.dot(B, x0)
    for i in range(n):
        xn[i] += d[i]
    while np.linalg.norm( np.subtract(xn, x0), np.inf) >= e1:
        x0 = xn
        xn = np.dot(B, x0)
        for i in range(n):
            xn[i] += d[i]
    return xn

def zeidel_method(n, a, b, eps):
    x0 = np.zeros(n)
    xn = np.zeros(n)
    B = np.zeros((n,n))
    d = np.zeros(n)

    for i in range(n):
        for j in range(n):
            if j == i:
                B[i][i] = 0
            else:
                B[i][j] = (-a[i][j] / a[i][i])
        d[i] = b[i] / a[i][i]

    e1 = (1 - np.linalg.norm(B, np.inf)) / np.linalg.norm(B, np.inf) * eps

    x0 = d
    for i in range(n):
        for j in range(n):
            if j < i:
                xn[i] += B[i][j] * xn[j]
            elif j > i:
                xn[i] += B[i][j] * x0[j]
    for i in range(n):
        xn[i] += d[i]
    while np.linalg.norm( np.subtract(xn, x0), np.inf) >= e1:
        x0 = xn
        xn = np.dot(B, x0)
        for i in range(n):
            xn[i] += d[i]
    return xn

def random_three_diagonal_matrix(n):
    a = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if j == i or j == i - 1 or j == i + 1:
                a[i][j] = np.random.normal()
    return a

def progonka_method(n, a, b):
    A, B = np.zeros(n), np.zeros(n)
    for i in range(n):
        if i == 0:
            y = a[i][i]
            A[i] = - (a[i][i+1] / y)
            B[i] = b[i] / y
        elif i == n-1:
            y = a[i][i] + a[i][i-1] * A[i-1]
            B[i] = (b[i] - a[i][i-1] * B[i-1]) / y
        else:
            y = a[i][i] + a[i][i-1] * A[i-1]
            A[i] = - (a[i][i+1] / y)
            B[i] = (b[i] - a[i][i-1] * B[i-1]) / y
    x = np.zeros(n)
    x[n-1] = B[n-1]
    for i in range(n-2, -1, -1):
        x[i] = A[i] * x[i+1] + B[i]
    return x

def check_ans(x, ans, eps):
    for i in range(len(x)):
        if np.fabs(x[i] - ans[i]) > eps:
            return False
    return True

def main():
    n = int(input("Enter n : "))
    eps = 1e-5
    #x, a = np.random.rand(n), np.random.rand(n,n)
    #x,a = np.array([1.102, 0.991, 1.101]), np.array([[10, 1, -1], [1, 10, -1], [-1, 1, 10]])
    #x,a = np.array([1.49, -0.02, -0.68]), np.array([[2, -1, 0], [5, 4, 2], [0, 1, -3]])
    #x,a = np.array([-3, 1, 5, -8]),np.array([[2,1,0,0],[1,10,-5,0],[0,1,-5,2], [0,0,1,4]])
    x,a = np.random.rand(n), random_three_diagonal_matrix(n)
    b = gen_matrix(n, x, a)
    print(a)
    xans = progonka_method(n, a, b)
    print (x, '\n', xans)
    print(check_ans(x, xans, eps))

if __name__ == "__main__":
    main()