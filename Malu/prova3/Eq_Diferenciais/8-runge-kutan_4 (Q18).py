""" Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=0.466 e y0=2.389. Use o método de Runge-Kutta de ordem 4 para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.107. """

def RK4_with_x_list(f, x0, y0, x_list, n):
    aux_list = [x0]
    aux_list.extend(x_list)
    x_list = aux_list
    r = []
    for i in range(1, n+1):
        m1 = f(x0,y0)
        h = (x_list[i]-x_list[i-1])
        m2 = f(x0 + h/2, y0 + (h/2) * m1)
        m3 = f(x0 + h/2, y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1+2 * m2 + 2 * m3 + m4)/6
        x0 = x_list[i]
        y0 = yk
        r.append((x0,y0))
    return r

def f(x,y):
    return y * (1 - x) + x + 2

x0 = 1.1511
y0 = 0.745
x_list = [1.1636, 1.2099, 1.2604, 1.3098, 1.3689, 1.4136, 1.4874, 1.5275, 1.584, 1.6151, 1.6656, 1.7237, 1.7869, 1.8241, 1.8616, 1.9336, 1.9853, 2.0114, 2.0605, 2.1404]
n = 20
r = RK4_with_x_list(f,x0,y0, x_list,n)
for xi, yi in r:
    print(yi, end = ", ")