""" Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=0.967 e y0=2.757. Use o método de Heun para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.196. """

def heun_with_x_list(f,x0,y0,x_list,n):
    aux_list = [x0]
    aux_list.extend(x_list)
    x_list = aux_list
    r = []
    for i in range(1, n+1):
        m1 = f(x0,y0)
        h = (x_list[i]-x_list[i-1])
        m2 = f(x0 + h, y0 + h * m1)
        y1 = y0 + h *(m1 + m2) / 2
        x0 = x_list[i]
        y0 = y1
        r.append((x0,y0))
    return r

def f(x,y):
    return y * (2 - x) + x + 1

x0, y0 = 1.63349, 0.61629
x_list = [1.65358, 1.72533, 1.75282, 1.81169, 1.85465, 1.89884, 1.97533, 1.99071, 2.04805, 2.1173, 2.1617, 2.18911, 2.25602, 2.32729, 2.371, 2.40204, 2.44873, 2.51476, 2.57491, 2.61787]
n = 20
e = heun_with_x_list(f,x0,y0, x_list,n)

for xi, yi in e:
    print(yi, end = ",")
