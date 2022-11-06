import numpy as np

# BEST_POLY

def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i+j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))

    print("Matriz dos coeficientes: ")
    for line in A:
        for item in line:
            print(item, end = ", ")
        print()
    print()
    
    print("Matriz dos termos independentes: ")
    for item in B:
        print(item, end=", ")
    print()
    print()
    return np.linalg.solve(A, B)


def eval_poly(x, coefs):
    s = coefs[0]
    for i, ci in enumerate(coefs[1:], 1):
        s += ci * x ** i
    return s

if __name__ == '__main__':

    x = [0.3279, 1.6466, 1.872, 3.3111, 3.4577, 4.4676, 5.4022, 6.568, 6.77, 7.9654, 8.4088, 9.6938]
    y = [5.336, 4.4452, 4.3651, 3.8293, 3.8644, 3.742, 3.9001, 4.218, 4.368, 5.1651, 5.3744, 6.4682]
    values = [0.4381, 3.0434, 4.8611]

    grau = 2

    coefs = best_poly(x, y, grau)

    print("Coeficientes: ")
    for c in coefs:
        print(c, end = ', ')
    print()
    
    print("P(x): ")
    for v in values:
        print(eval_poly(v, coefs), end = ", ")

    
