class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #Convertir a max-heap usando valores negativos
        max_heap = [-stone for stone in stones]
        #Convertir lista en un heap valido
        heapq.heapify(max_heap)

        #Continuar mientras haya al menos 2 piedras
        while len(max_heap) > 1: 
            #Extraer las 2 piedras 
            #negamos para obtener valores originales
            heaviest = -heapq.heappop(max_heap)
            second_heaviest = -heapq.heappop(max_heap)



            #Si son diferentes, queda 1 piedra con la diferencia
            if heaviest != second_heaviest: 
                heapq.heappush(max_heap, -(heaviest-second_heaviest))


        return -max_heap[0] if max_heap else 0 
