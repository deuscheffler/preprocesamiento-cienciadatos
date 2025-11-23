import time
import Codigo_original as original
import Codigo_optimizado as optimizado

# Código original
inicio = time.time()
# El archivo original debe ejecutar todo al importar
original
fin = time.time()
tiempo_original = fin - inicio

# Código optimizado
inicio = time.time()
optimizado
fin = time.time()
tiempo_opt = fin - inicio

print("Resultados de tiempo:")
print(f"Tiempo código ORIGINAL:   {tiempo_original:.4f} segundos")
print(f"Tiempo código OPTIMIZADO: {tiempo_opt:.4f} segundos")
