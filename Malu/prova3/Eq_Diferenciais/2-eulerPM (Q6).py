import numpy as np

def true_euler(f, x0, y0, h, n):
    for k in range(n):
        y0 += h * f(x0, y0)
        x0 += h        
        print(f'x_{k + 1}={x0} e y_{k+1}={y0}')

def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        x0 += h
        xk = x0 + k*h
        y0 += h * f(xk, y0)
        vals.append([xk,y0])
    return vals

def euler_mid_with_x_list(f, x0, y0, x_list, n):
    aux_list = [x0]
    aux_list.extend(x_list)
    x_list = aux_list
    for i in range(1, n+1):
        m1 = f(x0, y0)
        h = (x_list[i]-x_list[i-1])
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        y0 = y0 + h * m2
        x0 = x_list[i] 
        yield x0, y0

if __name__ == '__main__':
    def f(x, y):
        return y * (2 - x) + x + 1
    
    x0, y0 = 1.21386, 2.84458
    x_list = [1.24514, 1.2771, 1.35463, 1.39117, 1.44764, 1.47703, 1.53302, 1.60382, 1.64956, 1.68349, 1.72365, 1.77369, 1.8209, 1.8723, 1.93291, 1.9803, 2.05311, 2.08672, 2.1414, 2.2024] 
    n = 20
    #r1 = true_euler(f, x0, y0, h, n) #euler
    #print(r1)
    #x1, y1 = zip(*r1)
    #print(y1)

    r2 = euler_mid_with_x_list(f, x0, y0, x_list, n) #euler ponto medio
    x2, y2 = zip(*r2)
    print(y2)

    #plot 
    """
    import matplotlib.pyplot as plt
    t = np.linspace(x0, x0 + n * h, 200)
    yt = [y(ti) for ti in t]
    plt.plot(t, yt, color='blue')
    plt.scatter(x1, y1, color='orange')
    plt.scatter(x2, y2, color='magenta')
    plt.savefig('euler.png')
    """