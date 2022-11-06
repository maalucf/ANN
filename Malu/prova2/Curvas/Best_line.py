import numpy as np

def best_line(x, y):
    n = len(x)
    # soma das coordenadas x
    sum_x = sum(x)
    # soma das coordenadas x**2
    sum_x2 = sum(xi ** 2 for xi in x)
    # soma das coordenadas y
    sum_y = sum(y)
    #soma das coordenadas x*y
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    # Matriz dos coeficientes
    A = [[n, sum_x], [sum_x, sum_x2]]
    # Matriz dos termos independentes
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)

# exemplo:
x = [0.3069, 0.5748, 0.9311, 1.0792, 1.2675, 1.7837, 1.96, 2.2538, 2.5556, 2.8624, 3.1273, 3.6787, 3.7795, 4.2492, 4.6749, 4.887, 5.2187, 5.6176, 5.755, 6.0614, 6.485, 6.7373, 6.9091, 7.2435, 7.7807, 8.0065, 8.29, 8.6859, 8.7831, 9.2933, 9.6159, 9.7896]
y = [5.0202, 5.1347, 6.1902, 6.6458, 6.84, 7.8399, 8.0359, 8.546, 9.1698, 9.9186, 11.0054, 11.2605, 11.5514, 12.3542, 13.3458, 13.549, 14.2757, 15.0767, 15.2459, 16.8776, 16.7044, 17.2746, 17.3743, 18.1285, 18.9656, 19.4763, 19.9863, 20.973, 20.5522, 22.2054, 22.5808, 23.0279]

a0, a1 = best_line(x, y)

print(f'{a0}, {a1},')

# para calcular p(x) para alguns valores de x
def p(x, a0, a1):
    return a0 + a1 * x

values = [1.228, 4.3411, 4.8944, 5.7832, 6.5617]

for v in values:
    print(p(v, a0, a1), end = ', ')
