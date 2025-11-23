import cProfile
import pstats

import Codigo_optimizado as optimizado

with cProfile.Profile() as profile:
    optimizado

stats = pstats.Stats(profile)
stats.sort_stats(pstats.SortKey.TIME)
stats.dump_stats("profiling_optimizado.txt")

print("Profiling del código optimizado guardado en profiling_optimizado.txt")
