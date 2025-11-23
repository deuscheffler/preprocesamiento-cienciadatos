import math
import numpy as np
import time

inicio = time.time()


numeros = np.arange(1, 100001)


def es_primo(n):
    if n < 2:
        return False
    limite = int(math.sqrt(n)) + 1
    for i in range(2, limite):
        if n % i == 0:
            return False
    return True

es_primo_vec = np.vectorize(es_primo)


primos = [num for num, flag in zip(numeros, es_primo_vec(numeros)) if flag]

fin = time.time()
tiempo = fin - inicio

print("Cantidad de números primos encontrados:", len(primos))
print(f"Tiempo de ejecución: {tiempo:.4f} segundos")
