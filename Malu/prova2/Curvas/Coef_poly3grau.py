import numpy as np
# import scipy as sp

def best_poly (x, y, k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

    somas = {}
    somas[0] = n
    for n in range(1, 2*k + 1):
        somas[n] = sum(xi ** n for xi in x)
    A = []
    B = []
    for i in range (k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    return np.linalg.solve(A, B)

x = [-4.9317, -4.6795, -4.2869, -4.1048, -3.6256, -3.3906, -3.1576, -2.6547, -2.5848, -2.1699, -1.7785, -1.5705, -1.4476, -0.9863, -0.7215, -0.5276, -0.1423, 0.2289, 0.5566, 0.8443, 1.0163, 1.3739, 1.5509, 2.0541, 2.2135, 2.6268, 2.7078, 3.0638, 3.249, 3.66, 3.9226, 4.2295, 4.6419, 4.8876]
y = [6.345, 5.355, 6.2588, 6.0022, 6.8944, 6.6341, 7.0087, 6.5902, 6.8635, 7.2459, 6.7755, 5.1296, 5.9106, 6.3552, 7.1347, 5.1016, 5.8659, 6.177, 5.0795, 5.5538, 4.5991, 4.7929, 4.6512, 4.5729, 4.5863, 3.815, 3.5003, 4.4137, 4.479, 4.9227, 4.5791, 5.2963, 6.0786, 6.4837]

a0, a1, a2, a3 = best_poly(x, y, 3)

print(f'{a0} , {a1 }, {a2 }, {a3 }, ')

# para calcular p(x) para alguns valores de x
def p(x, a0, a1, a2, a3):
    return a0 + a1 * x + a2 * x**2 + a3 * x**3

values = [-3.8385, -3.6124, -2.4446, -2.3681, -1.3102]

for v in values:
    print(p(v, a0, a1, a2, a3), end = ', ')