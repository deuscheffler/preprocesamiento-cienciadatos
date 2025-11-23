import time
import matplotlib.pyplot as plt
import Codigo_original as original
import Codigo_optimizado as optimizado

tiempos_original = []
tiempos_opt = []

for _ in range(10):
    inicio = time.time()
    original
    tiempos_original.append(time.time() - inicio)

    inicio = time.time()
    optimizado
    tiempos_opt.append(time.time() - inicio)

plt.figure(figsize=(10,5))
plt.plot(tiempos_original, label="Original")
plt.plot(tiempos_opt, label="Optimizado")
plt.xlabel("Iteración")
plt.ylabel("Tiempo (segundos)")
plt.title("Distribución de tiempos por iteración")
plt.legend()
plt.show()
