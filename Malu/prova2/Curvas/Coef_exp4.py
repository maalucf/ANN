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
    return a * x * np.exp(b*x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [0.1752, 0.5523, 0.8291, 1.0604, 1.2657, 1.4312, 1.6496, 1.8999, 2.0996, 2.2628, 2.6425, 2.7946, 2.97, 3.2627, 3.4318, 3.791, 3.941, 4.254, 4.3843, 4.6464, 5.0476, 5.1921, 5.3222, 5.5861, 6.0013, 6.2047, 6.4581, 6.595, 6.8537, 7.021, 7.2612, 7.5291, 7.8044, 7.9973, 8.1408, 8.394, 8.7026, 9.0258, 9.0988, 9.2992, 9.6434, 9.9195]
    y = [0.7368, 2.028, 2.7716, 3.2858, 3.6934, 3.9972, 4.3221, 4.5422, 4.7189, 4.8737, 5.0824, 5.1863, 5.1355, 5.1732, 5.1785, 5.1819, 5.0513, 4.9409, 4.8785, 4.8769, 4.602, 4.5559, 4.5099, 4.3246, 4.1025, 4.0176, 3.799, 3.7362, 3.5781, 3.5045, 3.4266, 3.2057, 3.0401, 2.9451, 2.8572, 2.7223, 2.6597, 2.4113, 2.3713, 2.3387, 2.2134, 2.06]
    y_ = np.log(y) - np.log(x)
    x_ = x
    

    #   y = ax(e**(bx))
    #   log(y) = log(a) + log(x) + bx
    #   log(y)-log(x) = log(a) + bx
    #   a = b + cx

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    print(f'{a0 }, {a1}, ')

    a = np.exp(a0)
    b = a1 # para transformar a base do log, eh soh dividir pelo log desejado

    print()
    print(f'{a}, {b}, ')

    p = build_func(a, b)

    x_values = [1.3988, 3.3074, 3.6669, 6.4368, 9.3778]
 
    for xi_v in x_values:
        print(p(xi_v), end = ", ")