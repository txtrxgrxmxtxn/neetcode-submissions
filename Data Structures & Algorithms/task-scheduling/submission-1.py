from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Contar freq. 
        freq = Counter(tasks)


        #Encontrar la freq. máx.
        max_freq = max(freq.values())


        #contar cuantas tareas tienen la freq. max
        count_max = sum(1 for f in freq.values() if f == max_freq)


        #calc. ciclos min.

        cycles = (max_freq - 1) * (n+1) + count_max

        return max(cycles, len(tasks))
        