""" Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=0.776 e y0=0.981. Use o método de Ralston para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.131. """

def ralston(f, x0, y0, h,n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + 3/4 * h, y0 + m1 *3/4 * h )
        y0 += h * (m1 + 2 * m2) / 3
        x0 += h
        yield [x0,y0]

def f(x,y):
    return y * (2 - x) + x + 1

n = 15
h = 0.16967

x0, y0 = 1.61998, 0.90442

e = ralston(f,x0,y0, h, n)
for xi, yi in e:
    print(yi, end = ", ")