""" Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=0.466 e y0=2.389. Use o método de Runge-Kutta de ordem 4 para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.107. """

def RK4(f, x0, y0, h, n):
    aux_list = [x0]
    aux_list.extend(x_list)
    x_list = aux_list
    r = []
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + h/2, y0 + (h/2) * m1)
        m3 = f(x0 + h/2, y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1+2 * m2 + 2 * m3 + m4)/6
        x0 += h
        y0 = yk
        r.append((x0,y0))
    return r

def f(x,y):
    return y * (1 - x) + x + 2

x0 = 1.5489
y0 = 2.4635
h = 0.1958
n = 15
r = RK4(f,x0,y0, h,n)
for xi, yi in r:
    print(yi, end = ", ")