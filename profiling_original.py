import cProfile
import pstats

import Codigo_original as original  # tu archivo lento

with cProfile.Profile() as profile:
    original.es_primo(99991)  # prueba pequeña (opcional)
    original  # si ya ejecuta toda la lógica al import

stats = pstats.Stats(profile)
stats.sort_stats(pstats.SortKey.TIME)
stats.dump_stats("profiling_original.txt")

print("Profiling del código original guardado en profiling_original.txt")
