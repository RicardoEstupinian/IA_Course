import time
import sys

def factorial(n):
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta


def factorial_r(n):
    if(n == 1):
        return 1
    else:
        return n * factorial_r(n - 1)

if __name__ == '__main__':
    sys.setrecursionlimit(500000)
    n = 200000

    comienzo = time.time()
    factorial(n)
    final  = time.time()
    print(f'Resultado de tiempo 1: {final - comienzo}')

    comienzo = time.time()
    factorial_r(n)
    final  = time.time()
    print(f'Resultado de tiempo 2: {final - comienzo}')
