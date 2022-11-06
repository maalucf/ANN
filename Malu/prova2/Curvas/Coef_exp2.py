import numpy as np

def best_poly(x, y, grau = 1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if (p == 0):
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)

# alterar a funcao de acordo com a necessidade
def poly(x, a, b):
    return a * x**b

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [0.5395, 0.5969, 0.6678, 0.6976, 0.7608, 0.8261, 0.8803, 0.9217, 1.0188, 1.0421, 1.1499, 1.2064, 1.2688, 1.3125, 1.3818, 1.4045, 1.4649, 1.5698, 1.5895, 1.6431, 1.7439, 1.781, 1.8488, 1.9045, 1.9788, 2.0342, 2.0508, 2.1076, 2.1687, 2.2625, 2.2871, 2.3942, 2.42, 2.488, 2.5621, 2.6345, 2.6831, 2.7157, 2.7967, 2.8774, 2.9275, 2.9424]
    y = [0.3091, 0.052, 0.4918, 0.5554, 0.7742, 0.7779, 0.2619, 1.0947, 0.8024, 1.2289, 0.7259, 1.8127, 2.8246, 3.1988, 3.5341, 3.1608, 4.5589, 7.23, 5.8096, 6.2104, 8.1066, 8.4944, 9.9466, 10.6576, 12.9721, 14.3237, 14.2749, 15.5835, 16.8633, 20.5703, 21.6096, 25.7749, 26.1723, 29.1064, 32.6772, 36.1667, 38.3444, 40.3478, 45.5877, 50.2688, 53.1578, 54.9197]
    y_ = np.log(y)
    x_ = np.log(x)
 
    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    print(f'{a0 }, {a1}, ')

    a = np.exp(a0)
    b = a1 # para transformar a base do log, eh soh dividir pelo log desejado

    print()
    print(f'{a}, {b}, ')

    p = build_func(a, b)

    x_values = [1.4428, 1.5383, 2.1117, 2.7057, 2.7496]
 
    for xi_v in x_values:
        print(p(xi_v), end = ", ")