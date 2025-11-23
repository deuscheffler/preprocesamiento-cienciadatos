

import math
import time


inicio = time.time()



def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):  
        if n % i == 0:
            return False
    return True

primos = []


for numero in range(1, 100001):
    if es_primo(numero):
        primos.append(numero)

fin = time.time()

tiempo_total = fin - inicio

print("Cantidad de números primos encontrados:", len(primos))
print(f"Tiempo de ejecución (versión sin optimizar): {tiempo_total:.4f} segundos")