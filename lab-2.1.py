import numpy as np

def gen_stochastic_matrix(n):
    a = np.zeros((n, n))
    for i in range(n):
        r = 100
        for j in range(n):
            if (j == n-1 and i != j) :
                a[j][i] = r / 100.0
            elif (j == n-2 and i == n-1):
                a[j][i] = r / 100.0
            elif (i != j):
                rnd = np.random.random_integers(1, r)
                r -= rnd
                if (r == 0):
                    break
                a[j][i] = rnd / 100.0
    return a

def step_method(n, m, eps):
    r = np.full((n, 1), 1.0 / n)
    r1 = np.dot(m, r)
    r2 = np.dot(m, r1)
    q1 = r1[0] / r[0]
    q2 = r2[0] / r1[0]
    while (q2 - q1 > eps):
        r1 = r2
        r2 = np.dot(m, r1)
        q1 = q2
        q2 = r2[0] / r1[0]
    return r2

def main():
    n = int(input("Enter n : "))
    eps = 1e-2
    m = gen_stochastic_matrix(n)
    print (m)
    r = step_method(n, m, eps)
    print(r)

if __name__ == "__main__":
    main()
