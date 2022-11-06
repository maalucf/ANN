import math

def trapz(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a)
    soma += f(b)
    soma *= (h/2.0)
    print(f'Area aproximadamente: {soma}')

def f(x):
    return math.sqrt(math.sin(math.cos(math.log(x**2 + 1) + 2) + 3) + 4)

def trapzPonto(x, y):
    tam = len(x) - 1
    somas = 0
    for i in range(tam):
        h = x[i+1] - x[i]
        somas += (h/2) * (y[i] + y[i+1])
    print(f'Area = {somas}')

x = [0.187, 0.211, 0.348, 0.41, 0.437, 0.54, 0.684, 0.881, 0.907, 0.92, 1.051, 1.088, 1.546, 1.829, 1.972, 2.097, 2.142, 2.158, 2.163, 2.246, 2.386, 2.401, 2.559, 2.578, 2.833, 2.87, 2.955, 3.006, 3.313, 3.449, 3.498, 3.535, 3.611, 3.656, 3.658, 3.763, 4.001, 4.326, 4.406, 4.434, 4.437, 4.445, 4.559, 4.747, 4.855, 4.949, 4.994]
y = [1.855, 1.941, 2.401, 2.576, 2.643, 2.847, 2.987, 2.95, 2.93, 2.919, 2.784, 2.739, 2.205, 2.029, 2.001, 2.009, 2.02, 2.025, 2.027, 2.06, 2.148, 2.16, 2.307, 2.328, 2.64, 2.687, 2.791, 2.848, 2.988, 2.863, 2.782, 2.707, 2.52, 2.389, 2.383, 2.033, 1.241, 1.234, 1.526, 1.649, 1.663, 1.7, 2.262, 2.953, 2.956, 2.666, 2.445]

#intervalo = [1.733,4.952]
#subintervalos = [1, 22, 47, 50, 92, 138, 209, 263, 564, 972, 1845, 5145]

'''
n = len(subintervalos)
for i in range(n):
    trapz(f, intervalo[0], intervalo[1], subintervalos[i])
'''

trapzPonto(x, y)