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
    r = np.full((n, 1), 1 / n)
    r1 = np.dot(m, r)
    while (np.linalg.norm((r1 - r), ord = 1) - eps > 0):
        r = r1
        r1 = np.dot(m, r)
    return r1

def main():
    n = int(input("Enter n : "))
    eps = 1e-3
    m = gen_stochastic_matrix(n)
    print (m)
    r = step_method(n, m, eps)
    print(r)

if __name__ == "__main__":
    main()
