import numpy as np
import matplotlib.pyplot as plt

def pol_lagr_form(n, x, y, x0):
    L = 0
    for i in range(n):
        d1 = 1
        d2 = 1
        for j in range(n):
            if (j == i):
                continue
            d1 *= x0 -  x[j]
            d2 *= x[i] - x[j]
        L += y[i] * d1 / d2
    return L

def draw_lagr(n, x, y, a, b, eps):
    x_p = []
    y_p = []
    ind = 0
    while a <= b:
        x_p.append(a)
        y_p.append(pol_lagr_form(n, x, y, x_p[ind]))
        ind += 1 
        a += eps 

    plt.plot(x_p, y_p)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    return 

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

def cub_spline(n, x, y, eps):
    a = []
    b = []
    d = []
    h = []
    A = np.zeros((n,n))
    B = np.zeros(n)
    h.append(0)
    for i in range(1, n+1):
        a.append(y[i-1])
        h.append(x[i] - x[i-1])
    A[0][0] = 1
    A[n-1][n-1] = 1
    for i in range(1, n-1):
        A[i][i] = 2 * (h[i] + h[i+1])
        A[i][i-1] = h[i]
        A[i][i+1] = h[i+1]
        B[i] = 3 * ((y[i+1] - y[i]) / h[i+1] - (y[i] - y[i-1]) / h[i])
    c = progonka_method(n, A, B)

    for i in range(n-1):
        d.append( (c[i+1] - c[i]) / (3 * h[i+1]) )
        b.append( ((y[i+1] - y[i]) / h[i+1]) - (h[i+1] / 3) * (c[i+1] + 2 * c[i]) )
    d.append( -c[n-1] / (3 * h[n]) )
    b.append( ((y[n] - y[n-1]) / h[n]) - (2 * h[n] * c[n-1]) / 3 )

    x_p = []
    y_p = []
    ind = 0
    l = x[0]
    r = x[n]
    while l <= r:
        if (l>=x[ind+1]):
            ind += 1
        xx = l - x[ind]
        x_p.append(l)
        y_p.append(a[ind] + b[ind] * xx + c[ind] * xx * xx + d[ind] * xx * xx * xx )
        l += eps 

    plt.plot(x_p, y_p)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    return 

def newton_form(n, x, y, eps):
    a = []
    delta = y
    h = x[1] - x[0]
    fact = []
    fact.append(1)
    for i in range(1, n):
        fact.append(fact[i-1] * (i+1) )
    a.append(y[0])
    for i in range(n):
        for j in range(n-i):
            delta[j] = delta[j+1] - delta[j]
        a.append(delta[0] /  fact[i])

    x_p = []
    y_p = []
    l = x[0]
    r = x[n]
    while l <= r:
        x_p.append(l)
        S = 0
        q = 1
        for i in range(n+1):
            S += a[i] * q
            q *= (l - x[0]) / h - i
        y_p.append(S)
        l += eps 
    
    plt.plot(x_p, y_p)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    return 
#tests

#cub_splain and newton
# n = 6
# x = -1.5 -1 -0.5 0 0.5 1 1.5
# y = -0.7 0 0.7 1 0.7 0 -0.7

#lagr
# n = 7
# a = -1.5
# b = 1.5
# x = -1.5 -1 -0.5 0 0.5 1 1.5
# y = -0.7 0 0.7 1 0.7 0 -0.7

def main():
    eps = 0.2
    n = int(input("Enter n : "))
    #a = float(input("Enter a : "))
    #b = float(input("Enter b : "))
    x = [float(i) for i in input("Enter x_i: ").split()]
    y = [float(i) for i in input("Enter y_i: ").split()]
    cub_spline(n, x, y, eps)

if __name__ == "__main__":
    main()