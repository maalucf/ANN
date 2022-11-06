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
    return a * 2**(b * x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [0.0395, 0.1002, 0.1558, 0.1723, 0.2545, 0.3088, 0.3721, 0.4097, 0.4991, 0.5062, 0.5743, 0.6529, 0.6983, 0.7397, 0.8282, 0.8704, 0.8907, 0.9455, 1.0461, 1.1048, 1.125, 1.1984, 1.2529, 1.3177, 1.3343, 1.4009, 1.4458, 1.5182, 1.5813, 1.6431, 1.6977, 1.7526, 1.7782, 1.8564, 1.9235, 1.9778]
    y = [6.9723, 6.0307, 6.1572, 7.7435, 6.0342, 7.9579, 7.4659, 8.048, 9.0479, 8.8665, 9.2469, 10.6187, 12.5884, 11.7516, 12.4675, 12.7963, 15.9542, 11.3806, 13.9634, 17.0822, 17.7598, 19.1607, 20.8084, 21.9653, 21.9897, 24.3266, 25.8393, 27.6293, 28.913, 31.5172, 32.115, 35.9258, 36.6708, 40.2562, 43.0884, 44.6447]
    y_ = np.log(y)
 
    grau = 1

    a0, a1 = best_poly(x, y_, grau)

    print(f'{a0 }, {a1}, ')

    a = np.exp(a0)
    b = a1/np.log(2) # para transformar a base do log, eh soh dividir pelo log desejado

    print()
    print(f'{a}, {b}, ')

    p = build_func(a, b)

    x_values = [0.0759, 0.2919, 0.6541, 0.9924, 1.5418]
 
    for xi_v in x_values:
        print(p(xi_v), end = ", ")