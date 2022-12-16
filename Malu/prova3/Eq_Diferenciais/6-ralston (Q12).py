""" Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=0.776 e y0=0.981. Use o método de Ralston para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.131. """

def ralston_with_x_list(f, x0, y0, x_list,n):
    aux_list = [x0]
    aux_list.extend(x_list)
    x_list = aux_list
    for i in range(1, n + 1):
        m1 = f(x0, y0)
        h = (x_list[i]-x_list[i-1])
        m2 = f(x0 + 3/4 * h, y0 + m1 *3/4 * h )
        y0 += h * (m1 + 2 * m2) / 3
        x0 = x_list[i]
        yield [x0,y0]

def f(x,y):
    return y * (2 - x) + x + 1

n = 20
x_list = [1.97208, 2.03833, 2.07971, 2.13154, 2.16411, 2.23192, 2.2734, 2.346, 2.38238, 2.44884, 2.47246, 2.5218, 2.58432, 2.62656, 2.68803, 2.71174, 2.7722, 2.84087, 2.88293, 2.94604]

x0, y0 = 1.95435, 0.5551

e = ralston_with_x_list(f,x0,y0, x_list, n)
for xi, yi in e:
    print(yi, end = ", ")