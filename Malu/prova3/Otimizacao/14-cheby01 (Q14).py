import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols
from math import *

"""
Método de interpolação para ser usado nas raízes do polinômio de Chebyshev:
"""
def diff_div(X, Y):
    # Esta cópia de Y irá mudar a cada iteração:
    Y_table = [yi for yi in Y]  

    # Sabemos que o primeiro coeficiente, a0, é sempre igual a y0, assim temos:
    coeffs = [Y[0]] + [0 for yi in Y[1:]]   
    
    n = len(coeffs)
    
    # Para cada coluna (lembrando que a 1º coluna já é dada):
    for i in range(n-1):

        # Para cada elemento da coluna (lembrando que a0 já foi calculcado):
        for j in range(n - i - 1):
            num = Y_table[j+1] - Y_table[j]
            denom = X[j+1+i] - X[j]
            Y_table[j] = num/denom

        # Como Y_table a cada "for" se torna outra coluna da tabela, lembre-se...
        # ... que sempre o primeiro elemento de uma coluna k equivale ao coeficiente ak:
        coeffs[i+1] = Y_table[0]

    return coeffs

def build_poly(X, coeffs):
    def func(x):
        sum = 0
        for i, ci in enumerate(coeffs):
            prod = ci
            # Se i = 0 o loop não itera:
            for j in range(i):
                prod *= (x - X[j])
            sum += prod
        return sum
    return func

"""
Métodos de integração e de aproximação de funções para serem utilizados em conjunco com polinômios 
de Chebyshev:
"""

def simpson(f, a, b, num_subintervals):

    # Obs.: num_intervals(n) é o número de subintervalos, n/2 é o número de parábolas e n+1 é o número de pontos na partição.
    h = (b-a)/num_subintervals
    sum = f(a) + f(b)

    # k varia até 2n
    for k in range(2, num_subintervals, 2):
        sum += 2*f(a + k*h)

    # k varia até 2n-1 (quando k = 2n+1 o loop para)
    for k in range(1, num_subintervals, 2):
        sum += 4*f(a + k*h)

    sum = (h/3)*sum        
    return sum

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

def aprox_coeffs(func_list, f, a, b, n, k):
    A = []
    B = []
    # Obs.: note que a matriz A é simétrica portanto não precisamos calcular n² integrais
    for i, fi in enumerate(func_list):
        row = []
        b_i = richardson(lambda x: f(x)*fi(x), a, b, n, k)
        for j, fj in enumerate(func_list):
            """
            Note que:
            (1) a_ij = ∫ fj(x)*fi(x) dx;
            (2) visto que a matriz A é simétrica e a parte acima da diagonal é calculada primeiro,
            não é necessário calcular os elementos em que i > j.
            """
            if(i <= j):
                a_ij = richardson(lambda x: fi(x)*fj(x), a, b, n, k)
                row.append(a_ij)
            else:
                row.append(A[j][i])
                
        B.append(b_i)
        A.append(row)
    return np.linalg.solve(A, B)

def build_aprox_func(func_list, coeffs):
    def g(x):
        return sum(ck*fk(x) for ck, fk in zip(coeffs, func_list))
    return g

"""
Dentre todos os polinômios de grau n que interpolam y = f(x) numa lista de n+1 pontos no intervalo [-1, 1],
aquele que interpola nas raízes do polinômio T_n+1(x) é o polinômio que melhor se aproxima da função y = f(x),
ou seja, esse polinômio minimiza a seguinte função erro:

    erro(P) = max|f(x)-P(x)| para -1 <= x <= 1, sendo P um polinômio

"""

def changeToCheby(f, a, b):
    def F(u):
        return f(((b-a)/2) * u + (a+b)/2)
    return F

def changeFromCheby(g, a, b):
    def G(u):
        return g((2/(b-a)) * u - (a+b)/(a-b))
    return G

def getChebyPoly(n):
    """
    Retorna o e-nésimo polinômio de chebyshev como um objeto de expressão
    da biblioteca sympy (o que é diferente e melhor que um função recursiva
    com complexidade O(2^n)).
    """
    x = symbols('x')
    t_n = 1
    T = [1, x]
    for _ in range(1, n):
        t_n = 2*T[1]*x - T[0]
        T = [T[1], t_n]
    return t_n

def getChebyPolyList(n):
    """
    Retorna a lista do n primeiros polinômios de chebyshev como objetos de expressão
    da biblioteca sympy (o que é diferente e melhor que um função recursiva com complexidade O(2^n)).
    """
    x = symbols('x')
    t_n = 1
    T = [1, x]
    for i in range(2, n):
        t_n = 2*T[i-1]*x - T[i-2]
        T.append(t_n)
    return T

def chebyRoots(n):
    """
    Retorna as n raízes do e-nésimo polinômio de chebyshev.
    """
    roots = []
    for k in range(1, n+1):
        x_k = cos((2*k-1)*pi/(2*n))
        roots.append(x_k)
    return roots

def stringToFunc(string):
    def f(x):
        return eval(string)
    return f


if __name__ == '__main__':

    # Exemplo 01:

    # def f(x):
    #     return x * sin(-6 * x**2)

    # a = -1
    # b = 1

    # n = 4
    # X = chebyRoots(n+1)
    # Y = [f(xi) for xi in X]

    # coeffs = diff_div(X,Y)
    # p = build_poly(X, coeffs)

    # t = np.linspace(-1, 1, 200)
    # ft = [f(ti) for ti in t]
    # pt = [p(ti) for ti in t]

    # plt.plot(t, ft, color = "green", label = "f(x)")
    # plt.plot(t, pt, color = "blue", label = "g(x)")
    # plt.legend()
    # plt.savefig("Exemplo01.png")
    # plt.close()

    # Exemplo 02:

    def f(x):
        return tanh(3*x) * cos(3*x) 

    a = -1
    b = 1
    n = 10
    num_poly_cheb = 16

    x = symbols('x')
    T = getChebyPolyList(num_poly_cheb)
    for i in range(0, len(T)):
        T[i] = stringToFunc(str(T[i]))

    k = 8
    coeffs = aprox_coeffs(T, f, a, b, n, k)
    for ck in coeffs: 
        print(f"{ck},")

    g = build_aprox_func(T, coeffs)
    values = [-0.425, 0.227, 0.717]

    for xi in values:
        print(f"{g(xi)},")

    n = 1024
    print(simpson(lambda x: (f(x)-g(x))**2, a, b, n))

    # Exemplo03 (tentanto fazer mudança de variável):

    # def f(x):
    #     return x * sin(-6 * x**2)

    # a = -1
    # b = 1

    # f_cheby = changeToCheby(f, a, b)

    # n = 4
    # X = chebyRoots(n+1)
    # Y = [f_cheby(xi) for xi in X]

    # coeffs = diff_div(X,Y)
    # p = build_poly(X, coeffs)

    # g = changeFromCheby(p, -2, 2)

    # t = np.linspace(-2, 2, 200)
    # ft = [f(ti) for ti in t]
    # gt = [g(ti) for ti in t]

    # plt.plot(t, ft, color = "green", label = "f(x)")
    # plt.plot(t, gt, color = "blue", label = "g(x)")
    # plt.legend()
    # plt.savefig("cheby.png")
    # plt.close()