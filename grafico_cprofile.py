import pstats
import matplotlib.pyplot as plt

def graficar_cprofile(archivo, titulo, top=10):
    """
    Genera un gráfico de barras con las funciones que más tiempo consumieron
    según un archivo de cProfile (.txt).
    """

    # Cargar estadísticas
    stats = pstats.Stats(archivo)
    stats.sort_stats(pstats.SortKey.TIME)

    # Obtener datos del top de funciones más costosas
    funciones = []
    tiempos = []

    for func, info in list(stats.stats.items())[:top]:
        tiempo_total = info[2]  # tiempo total en la función
        nombre_func = f"{func[2]}:{func[1]}"  # nombre y línea
        funciones.append(nombre_func)
        tiempos.append(tiempo_total)

    # Crear gráfico
    plt.figure(figsize=(10, 6))
    plt.barh(funciones, tiempos)
    plt.xlabel("Tiempo total (segundos)")
    plt.ylabel("Función")
    plt.title(titulo)
    plt.gca().invert_yaxis()  # La función más lenta arriba
    plt.tight_layout()
    plt.show()


# -------------------------------------------
# Ejemplos de uso
# -------------------------------------------

graficar_cprofile(
    "profiling_original.txt",
    "Funciones más costosas - Código Original",
    top=10
)

graficar_cprofile(
    "profiling_optimizado.txt",
    "Funciones más costosas - Código Optimizado",
    top=10
)
