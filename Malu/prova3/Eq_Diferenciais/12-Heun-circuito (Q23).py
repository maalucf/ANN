from cmath import sin
import math

from numpy import mat


def heun(f, x0:float, y0:float, h, n):
    r = []
    for _ in range(1,n+1):
        #realizar as iterações
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h*m1)
        y1 = y0 + h * (m1+m2)/2
        #atualizando os valores
        x0 += h
        y0 = y1
        #colocando valores na lista
        print(str(y0.real),",", end='')
        r.append((x0, y0))
    return r

if __name__ == "__main__":
    def f(x, y):
        k = -0.0707
        der1=-math.exp(k*math.pi*x)*(2*math.cos(2*x) + k*math.pi*math.sin(2*x))
        der2=-math.exp(k*math.pi*x)*(4*k*math.pi*math.cos(2*x) + (k**2*math.pi**2-4) *math.sin(2*x))
        e=math.exp(k*math.pi*x)*math.sin(2*x-math.pi)
        c = 0.2497
        r = 1.4996
        l = 1.8881
        return c*der2+(der1/r)+(e/l)

    x0 = 0
    y0 = 0
    h = 0.1831
    n = 150
    r = heun(f, x0, y0, h, n)
    # print(r)