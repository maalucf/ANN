import matplotlib.pyplot as plt
import numpy as np
from math import *

def richardson(f, a, b, n, k):
    table = []
    # Obs.: dada essa função de erro inicial tem-se que Fk(h) diminui o erro para O(h^(2*k))
    k = int(k/2)

    for i in range(k):
        item = trapeze_sum(f, a, b, (2**i)*n)
        table.append(item)

    for i in range(k):
        for j in range(k-i-1):
            new_item = ((4**(i+1))*table[j+1] - table[j])/(4**(i+1) - 1)
            table[j] = new_item

    return table[0]


def trapeze_sum(f, a, b, n):
    sum = f(a)/2 + f(b)/2
    base = (b-a)/n
    # Lembre-se que x0 = a e xn = b, por isso no seguinte loop k varia de 1 até n-1:
    for k in range(1, n):
        sum += f(a + k*base)
    area = base*sum
    return area

def fourier_coeffs(f, a, b, num_coeffs, num_intervals):
    """
    Retorna os coeficientes a_n's, b_n's e c da série de fourier 
    para uma determinada função f(x)
    """   
    A = []
    B = []

    c = (1/(2*pi))*trapeze_sum(f, a, b, num_intervals)

    for m in range(1, num_coeffs+1):
        a_m = (1/pi)*trapeze_sum(lambda x: f(x)*cos(m*x), a, b, num_intervals)
        b_m = (1/pi)*trapeze_sum(lambda x: f(x)*sin(m*x), a, b, num_intervals) 
        A.append(a_m)
        B.append(b_m)

    return A, B, c

def build_fourier(A, B, c):
    """
    Monta a série de fourier a partir dos coeficientes a_n's, b_n's e c
    calculados para um determinada função f(x)
    """
    def f(x):
        return c + sum(a_n*cos(n*x) + b_n*sin(n*x) for n, (a_n, b_n) in enumerate(zip(A, B), 1))
    return f

if __name__ == "__main__":
    
    def f(x):
        return x * sin(6*e**(-x**2))

    num_intervals = 1024
    num_coeffs = 5
    a = -pi
    b = pi

    A, B, c = fourier_coeffs(f, a, b, num_coeffs, num_intervals)
    # print(f"A = {A}\n B = {B}\n c = {c}")
    print(f"{c},")
    for a_n, b_n in zip(A, B):
        print(f"{a_n}, {b_n},")
    
    g = build_fourier(A, B, c)
    values = [-2.463, 0.665, 2]
    for i, xi in enumerate(values):
        print(f"g(x_{i+1}) = {g(xi)}")

    k = 8
    num_intervals = 10 
    erro = richardson(lambda x: (f(x)-g(x))**2, a, b, num_intervals, k)
    print(erro)
    # Lembre-se que num_intervals = (b-a)/h


    t = np.linspace(-pi, pi, 200)
    ft = [f(ti) for ti in t]
    gt = [g(ti) for ti in t]

    # plt.plot(t, ft, color='green', label='f(x)')
    # plt.plot(t, gt, color='blue', label='Fourier Serie for f(x)')
    # plt.legend()
    # plt.savefig("fourier01.png")
    # plt.close()