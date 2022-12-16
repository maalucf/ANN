""" Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=1.053 e y0=1.787. Use o método de Runge-Kutta de ordem 2 com b=0.53 para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.175. """

def RK2_with_x_list(f, x0, y0, x_list, n, b):
    aux_list = [x0]
    aux_list.extend(x_list)
    x_list = aux_list
    a = 1 - b
    p = 1 / (2 * b)
    q = p
    for i in range(1, n+1):
        m1 = f(x0,y0)
        h = (x_list[i]-x_list[i-1])
        m2 = f(x0+p*h, y0+q*h*m1)
        y0 += (a * m1 + b * m2) * h
        x0 = x_list[i]
        yield [x0,y0]

def f(x,y):
    return y * (1 - x) + x + 2

x0, y0 = 1.89792, 2.22333
x_list = [1.93364, 1.98856, 2.00726, 2.0603, 2.11733, 2.17544, 2.2178, 2.26843, 2.32728, 2.36723, 2.41394, 2.46237, 2.53907, 2.5844, 2.6299, 2.6729, 2.71561, 2.77071, 2.82993, 2.88245]
b = 0.8235
n = 20

e = RK2_with_x_list(f,x0,y0, x_list,n, b)
for xi, yi in e:
    print(yi, end = ", ")