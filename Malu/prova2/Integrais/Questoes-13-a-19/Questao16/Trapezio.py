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
    return (9 + 4*(math.cos(0.49*x)**2))*(5*math.exp(-0.52*x) + 2*math.exp(0.18*x))

def trapzPonto(x, y):
    tam = len(x) - 1
    somas = 0
    for i in range(tam):
        h = x[i+1] - x[i]
        somas += (h/2) * (y[i] + y[i+1])
    print(f'Area = {somas}')

x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
y = [0, 104, 232, 361, 505, 673, 823, 967, 1092, 1202, 1326, 1462, 1628, 1819, 2055, 2308, 2594, 2900, 3203]

_x = []
m = len(x)
for xi in range(m):
  _x.append(x[xi]/3600)


a = 0
b = 90
n = 19

#trapz(f, a, b, n)
trapzPonto(_x, y)