import matplotlib.pyplot as plt


tiempo_original = 43.8971 
tiempo_opt = 0.2243         


plt.figure(figsize=(8,5))
plt.bar(["Original", "Optimizado"], [tiempo_original, tiempo_opt])
plt.ylabel("Tiempo (segundos)")
plt.title("Comparación de tiempos: Código Original vs Optimizado")
plt.show()
