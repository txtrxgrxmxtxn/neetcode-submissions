class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.min_heap = []

        #Agregar numeros iniciales al heap
        for num in nums: 
            self.add(num)
        

    def add(self, val: int) -> int:
        #Agregar el nuevo valor al heap 
        heapq.heappush(self.min_heap, val)

        #Si el heap excede k elem. remover el más pequeño
        if len(self.min_heap) > self.k: 
            heapq.heappop(self.min_heap)


        #el minimo del heap es el k-esimo más grande
        return self.min_heap[0]
