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

x = [-4.7279, -4.6706, -4.3385, -4.0378, -3.7743, -3.304, -3.175, -2.8608, -2.5579, -2.205, -2.0797, -1.7372, -1.3252, -1.1999, -0.8709, -0.5803, -0.2657, 0.0751, 0.2544, 0.7345, 1.076, 1.2327, 1.6307, 1.706, 1.9524, 2.3068, 2.7535, 2.979, 3.2049, 3.5328, 3.8367, 4.2206, 4.3421, 4.7623, 4.8425, 5.4195, 5.64, 5.7866]
y = [-3.9814, -3.3542, -1.4401, -0.3309, 0.6318, 1.6101, 2.4366, 1.8265, 1.515, 1.3523, 1.1611, 1.0577, 0.4971, 0.4445, -0.1822, -0.3784, 0.4488, -0.7175, -2.3282, -0.491, 0.0453, 0.1832, 0.9744, 0.7904, 1.6536, 2.2788, 3.4041, 3.8248, 3.1157, 3.563, 3.4764, 3.2167, 2.994, 1.743, 0.9791, -3.3752, -5.2666, -6.5777]

a0, a1, a2, a3, a4 = best_poly(x, y, 4)

print(f'{a0} , {a1}, {a2}, {a3}, {a4}, ')

# para calcular p(x) para alguns valores de x
def p(x, a0, a1, a2, a3, a4):
    return a0 + a1 * x + a2 * x**2 + a3 * x**3 + a4 * x**4

values = [-3.8844, -2.2745, 2.6421, 2.9081, 3.5898]

for v in values:
    print(p(v, a0, a1, a2, a3, a4), end = ', ')