import heapq

class MedianFinder:
    def __init__(self):
        # Max-heap para la mitad inferior (usamos negativos)
        self.small = []
        # Min-heap para la mitad superior
        self.large = []
    
    def addNum(self, num: int) -> None:
        # Agregar a small (max-heap)
        heapq.heappush(self.small, -num)
        
        # Mover el mayor de small a large
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Balancear: small debe tener igual o un elemento más que large
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def findMedian(self) -> float:
        # Si small tiene más elementos, la mediana es su tope
        if len(self.small) > len(self.large):
            return -self.small[0]
        # Si están balanceados, promediar los topes
        return (-self.small[0] + self.large[0]) / 2