class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix) #no. filas
        n = len(matrix[0]) #no. columnas.



        #Busqueda binaria en el array 'aplanado'
        left = 0
        right = m * n - 1

        while left <= right: 
            mid = (left + right) // 2 

            #convertir indice lineal a coord. de matriz
            row = mid // n 
            col = mid % n

            if matrix[row][col] == target:
                return True 
            elif matrix[row][col] < target: 
                left = mid + 1
            else: 
                right = mid - 1

        return False 




        