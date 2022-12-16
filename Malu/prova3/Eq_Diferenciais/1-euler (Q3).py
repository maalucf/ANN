import math
import matplotlib.pyplot as plt
import numpy as np

def euler_with_x_list(f, x0, y0, x_list, n):
    result = []
    aux_list = [x0]
    aux_list.extend(x_list)
    x_list = aux_list
    for i in range(1, n+1):
        y0 += f(x_list[i-1], y0) * (x_list[i]-x_list[i-1])
        result.append([x_list[i], y0])
        print(y0, end = ", ")
        #print(x0,y0)
        #print(f'x_{i+1} = {x_list[i]} \t||\t y_{i+1} = {y0}')
    return result

if __name__ == '__main__':

    def f(x, y):
        return y * (1 - x) + x + 2

    x0, y0 = 1.26203, 1.14728
    x_list =  [1.30104, 1.34418, 1.40207, 1.42739, 1.4809, 1.53845, 1.59003, 1.65088, 1.68128, 1.75489, 1.80427, 1.83692, 1.8864, 1.93356, 1.97323, 2.03171, 2.09609, 2.12832, 2.2006, 2.25396]
    n = 20

    #P3.7
    # def f(x, y):
    #     return y*(1 - x) + x + 2

    # x0, y0 = 1.47205, 2.16382
    # h = 0.13102
    # n = 10

    resposta = euler_with_x_list(f, x0, y0, x_list, n)

    def y(x):
        return 5 * math.exp(x - 1) - x - 2

    ##Visualizacao
""" t = np.linspace(x0, x0 + n * h, 100)
    yt = [y(i) for i in t]

    cx, cy = zip(*resposta)

    plt.plot(t, yt)
    plt.scatter(cx, cy)
    plt.savefig('euler.png') """