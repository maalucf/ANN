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

x = [0, 5/3600, 10/3600, 15/3600, 20/3600, 25/3600, 30/3600, 35/3600, 40/3600, 45/3600, 50/3600, 55/3600, 60/3600]
y = [182.48, 260.97, 244.52, 163.51, 117.68, 230.96, 141.07, 109.89, 151.17, 277.63, 205.58, 220.49, 292.51]

a = 0
b = 60
n = 19

#trapz(f, a, b, n)
trapzPonto(x, y)