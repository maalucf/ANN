import math
from numpy import double

# Usado para aproximar o valor de uma integral
def trapz(f, a, b, n):
    h = (b-a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma


def f(x):
    return math.sin(x/(math.sqrt(x**2 + 1))) + 1

# Variável inferior
a = -1.387
# Variável superior
b = 1.815

# Lista de subintervalos
n = [1, 16, 30, 69, 89, 126, 208, 397, 683, 982, 2406, 9013]

for i in range(len(n)):
    r = trapz(f, a, b, n[i])
    print(r, end = ", ")