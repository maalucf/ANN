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

x = [0.0941, 0.31, 0.7537, 0.8375, 1.2841, 1.4728, 1.6757, 2.1177, 2.2386, 2.5883, 2.991, 3.2096, 3.43, 3.8528, 4.1122, 4.2195, 4.5306, 4.7764, 5.1258, 5.3742, 5.6033, 5.9266, 6.3376, 6.54, 6.8213, 6.9525, 7.4252, 7.6907, 8.0346, 8.09, 8.571, 8.7683, 8.9988, 9.2561, 9.4794, 9.8327]
y = [5.8583, 5.4741, 5.0869, 5.0385, 4.3053, 4.6035, 4.3121, 4.156, 4.0934, 3.9459, 3.9904, 3.6788, 3.5535, 3.3885, 3.3571, 3.4225, 3.2007, 3.2384, 3.1687, 3.1094, 3.0769, 3.0884, 3.2117, 3.295, 3.4166, 3.2602, 3.2937, 3.6272, 3.5708, 3.5231, 3.7876, 3.8909, 3.8921, 4.0393, 4.1889, 4.4692]

a0, a1, a2 = best_poly(x, y, 2)

print(f'{a0} , {a1}, {a2},')

# para calcular p(x) para alguns valores de x
def p(x, a0, a1, a2):
    return a0 + a1 * x + a2 * x**2

values = [0.8047, 4.5596, 6.0345, 7.849, 8.3447]

for v in values:
    print(p(v, a0, a1, a2), end = ', ')