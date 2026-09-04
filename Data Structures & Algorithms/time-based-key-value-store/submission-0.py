class TimeMap:

    def __init__(self):
        self.datos = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.datos: 
            self.datos[key] = []
        self.datos[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.datos:
            return ""
        

        lista = self.datos[key]
        left = 0
        right = len(lista)-1
        result = -1 #indice del timestamp mas grande ≤ timestamp



        #busqueda binaria
        while left <= right: 
            mid = (left + right) // 2 
            if lista[mid][0] <= timestamp: #candidato valido, buscar + a la derecha
                result = mid 
                left = mid + 1 

            else: 
                right = mid - 1

        if result == -1: 
            return ""


        return lista[result][1]
            












        
