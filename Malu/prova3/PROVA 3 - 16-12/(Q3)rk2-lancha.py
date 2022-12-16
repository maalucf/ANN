from cmath import sqrt
import math
def rk4(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        #realizar as iterações
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + (h/2)*m1)
        m3 = f(x0 + h/2, y0 + (h/2)*m2)
        m4 = f(x0 + h, y0 + h *m3)
        yk = y0 + h * (m1+2*m2+2*m3+m4)/6
        #atualizando os valores 
        x0 += h
        y0 = yk
        #colocando valores na lista
        #print(y0)

        r.append((x0, y0))
    return r

def euler(f, x0, y0, h, n):
    result = []
    for i in range(n):
        y0 += f(x0, y0) * h
        x0 = h*(i+1)
        result.append([x0, y0])
        print(y0.real, end = ", ")
        #print(x0,y0)
        # print(f'x_{i+1} = {x0} \t||\t y_{i+1} = {y0}')
    return result



def rk2(f, x0, y0, h, n, b):
    vals = []
    a=1-b
    p=1/(2*b)
    q=p
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0+q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        #print(y0.real, end = ", ")
        vals.append([x0, y0])
    return vals

if __name__ == "__main__":

    def f(x, y):
        a = 8.12075
        return -(y/(sqrt(a**2 - y**2)))
    
    x0 = 1.0029
    y0 = 4.21487
    h = 0.08433
    b = 0.80864
    n = 100
    r = euler(f, x0, y0, h , n)
    # print(r)