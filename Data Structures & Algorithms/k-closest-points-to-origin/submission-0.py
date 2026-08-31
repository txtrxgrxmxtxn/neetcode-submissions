class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points: 
            #Calcular distancia
            distance = x*x + y*y


            #Usar dist. negativa para simular max-heap
            heapq.heappush(max_heap, (-distance, x, y))


            #Mantener solo k puntos más cercanos.
            if len(max_heap) > k:
                heapq.heappop(max_heap) #remover mas lejano


        return [[x, y] for _, x, y in max_heap]