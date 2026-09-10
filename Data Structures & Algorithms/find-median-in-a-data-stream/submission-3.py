import heapq

class MedianFinder: 
    def __init__(self):
        #Max-heap para la mitad inf. (usamos negativos)
        self.small = []


        #min-heap para la mitad sup.
        self.large = []


    def addNum(self, num: int) -> None:
        #agregar a small (max-heap)
        heapq.heappush(self.small, -num)


        #mover el mayor de small a large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        #Balancear: small debe tener igual o un elemento mas que large
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))


    def findMedian(self) -> float:
        #si small tiene mas elementos, la mediana es su tope 
        if len(self.small) > len(self.large):
            return -self.small[0]

        #si estan balanceados, promediar topes
        return (-self.small[0] + self.large[0])/2