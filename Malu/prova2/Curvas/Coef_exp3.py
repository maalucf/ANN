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
    return a * (x/(x + b))

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [1.0233, 1.7231, 1.9653, 2.7986, 3.0276, 3.3153, 4.0215, 4.5428, 4.798, 5.4719, 5.9038, 6.0773, 6.6247, 7.1972, 7.5702, 7.8487, 8.5148, 9.0324, 9.2564, 9.7446, 10.2858, 10.8358, 11.0845, 11.4942, 12.2826, 12.4326, 13.1746, 13.5195, 14.0133, 14.5578, 14.6282, 15.035, 15.7264, 16.2414, 16.4374, 16.8972, 17.3003, 17.779, 18.6134, 18.7507, 19.165, 19.7711]
    y = [0.6101, 0.8821, 0.9588, 1.1602, 1.2141, 1.3168, 1.4547, 1.4995, 1.514, 1.6623, 1.6664, 1.7143, 1.7618, 1.8418, 1.8184, 1.8784, 1.9333, 1.9524, 1.9794, 1.9521, 2.0363, 2.0482, 2.1362, 2.0929, 2.1833, 2.1442, 2.1851, 2.1757, 2.1944, 2.224, 2.2137, 2.2622, 2.2235, 2.302, 2.3091, 2.2987, 2.3507, 2.3378, 2.3786, 2.3643, 2.2729, 2.2775]
    y_ = [1/i for i in y]
    x_ = [1/i for i in x]
 
    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    print(f'{a0 }, {a1}, ')

    a = 1/a0
    b = a*a1 # para transformar a base do log, eh soh dividir pelo log desejado

    print()
    print(f'{a}, {b}, ')

    p = build_func(a, b)

    x_values = [2.7038, 3.564, 4.7075, 5.4708, 17.0396]
 
    for xi_v in x_values:
        print(p(xi_v), end = ", ")