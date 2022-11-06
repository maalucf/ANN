import math

def simps(f, a, b, n):
    if n % 2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior q 1")
    h = (b - a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1,n,2):
        soma_odd += f(a+k*h)
    for k in range(2,n,2):
        soma_even += f(a + k * h)
    return (h/3) * (f(a) + 4 * soma_odd + 2 * soma_even + f(b))

def simp(x0,x1,x3,y0,y1,y2):
    return ((x1-x0)/3)*(y0+4*y1+y2)

def simpsPonto(x, y):
    tam = (len(x) - 1) // 2
    somas = 0
    k = 0
    for i in range(tam):
        somas += simp(x[k],x[k+1],x[k+2],y[k],y[k+1],y[k+2])
        k += 2
    print(f'{somas}')

def f(x):
    return math.sqrt(1 + math.cos(x)**2)

intervalo = [-1.091, 1.438]
subintervalos = [4, 18, 32, 60, 98, 108, 132, 152, 194, 212, 278]

'''
n = len(subintervalos)
for i in range(n):
    print(simps(f, intervalo[0], intervalo[1], subintervalos[i]))
'''
x = [0.069, 0.4985, 0.928, 1.0395, 1.151, 1.2025, 1.254, 1.26, 1.266, 1.331, 1.396, 1.577, 1.758, 1.783, 1.808, 1.8425, 1.877, 1.9695, 2.062, 2.285, 2.508, 2.531, 2.554, 2.576, 2.598, 2.737, 2.876, 2.8975, 2.919, 2.944, 2.969, 3.232, 3.495, 3.5215, 3.548, 3.6065, 3.665, 3.925, 4.185, 4.269, 4.353, 4.434, 4.515, 4.6545, 4.794]
y = [1.446, 2.775, 2.912, 2.797, 2.66, 2.594, 2.528, 2.521, 2.513, 2.433, 2.357, 2.178, 2.059, 2.047, 2.037, 2.025, 2.015, 2.001, 2.004, 2.081, 2.255, 2.278, 2.302, 2.326, 2.35, 2.517, 2.694, 2.721, 2.748, 2.778, 2.807, 2.999, 2.787, 2.736, 2.678, 2.532, 2.361, 1.465, 1.002, 1.094, 1.321, 1.649, 2.042, 2.691, 2.999]
simpsPonto(x, y)