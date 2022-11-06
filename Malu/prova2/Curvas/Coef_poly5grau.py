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

x = [-4.4403, -4.2447, -4.0601, -3.6348, -3.4975, -3.3073, -3.0608, -2.8706, -2.5769, -2.4017, -2.2446, -2.027, -1.823, -1.4751, -1.264, -1.0164, -0.8921, -0.7314, -0.4945, -0.2339, 0.0996, 0.2979, 0.4406, 0.7209, 0.8993, 1.1201, 1.3108, 1.507, 1.7826, 1.9692, 2.2261, 2.3782, 2.5849, 2.7682, 2.9751, 3.2547, 3.525, 3.6678, 3.8587, 4.249, 4.4096]
y = [-7.6107, -3.6271, -0.9534, 2.6909, 3.0269, 3.1891, 2.9747, 2.8064, 1.788, 1.4873, 1.1269, 0.2468, -0.2175, -1.8755, -1.5108, -1.3706, -1.0053, -1.3799, -0.0016, -0.9792, 0.3631, 0.5109, 0.7802, -0.6418, 1.2572, 1.9753, 1.9956, 1.8412, 0.5568, -0.1132, -1.0583, -1.1282, -2.0837, -3.3581, -3.1238, -3.5642, -2.1162, -2.3491, -1.1172, 3.678, 6.2327]

a0, a1, a2, a3, a4, a5 = best_poly(x, y, 5)

print(f'{a0 } , {a1 }, {a2 }, {a3 }, {a4 }, {a5 }, ')

# para calcular p(x) para alguns valores de x
def p(x, a0, a1, a2, a3, a4, a5):
    return a0 + a1 * x + a2 * x**2 + a3 * x**3 + a4 * x**4 + a5 * x**5

values = [-3.3887, -1.3803, -1.3216, 1.4372, 2.1686]

for v in values:
    print(p(v, a0, a1, a2, a3, a4, a5), end = ', ')