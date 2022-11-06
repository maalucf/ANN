import math
import numpy as np

def richardson(col_1):
    n = len(col_1) - 1
    for i in range(n - 1):
        for j in range(n - 1 - i):
            numer = 2 ** (i + 1) * col_1[j + 1] - col_1[j]
            denom = 2 ** (i + 1) - 1
            value = numer / denom
            col_1[j] = value
    return col_1[0]

if __name__ == '__main__':
    approximations = [0.1765375302628862, 0.1982294389999817, 0.20827093818562226, 0.21308596160254467, 0.21544159464075818, 0.21660639345465427]
    
    new_value = richardson(approximations.copy())
    aprox = richardson(approximations + [new_value])
    print(aprox)
