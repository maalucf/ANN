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
    return b + np.log(x)*a

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [1.4264, 2.3024, 3.0448, 3.6116, 4.3662, 5.3241, 6.119, 6.6131, 7.0858, 8.1114, 8.805, 9.4717]
    y = [6.0842, 7.8326, 8.9059, 9.5498, 10.2396, 10.9551, 11.527, 11.6318, 12.1238, 12.5438, 12.8165, 13.1256]
    y_ = y
    x_ = np.log(x)

    #   x = e**((y-b)/a))
    #   log(x) = (y-b)/a
    #   log(x)*a + b= y
    #   y = b + log(x)*a
    
    #   a = b + cx

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    print(f'{a0 }, {a1}, ')

    a = a1
    b = a0 # para transformar a base do log, eh soh dividir pelo log desejado

    print()
    print(f'{a}, {b}, ')

    p = build_func(a, b)

    x_values = [3.0659, 5.0534, 8.4799]
 
    for xi_v in x_values:
        print(p(xi_v), end = ", ")