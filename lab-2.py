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


def check_ans(x, ans, eps):
    for i in range(len(x)):
        if np.fabs(x[i] - ans[i]) > eps:
            return False
    return True

def main():
    n = int(input("Enter n : "))
    eps = 1e-5
    #x, a = np.random.randint(1, 10, size=(n)), np.random.randint(1, 10, size=(n,n))
    x,a = np.array([1.102, 0.991, 1.101]), np.array([[10, 1, -1], [1, 10, -1], [-1, 1, 10]])
    b = gen_matrix(n, x, a)
    xans = zeidel_method(n, a, b, eps)
    print (x, '\n', xans)
    print(check_ans(x, xans, eps))

if __name__ == "__main__":
    main()