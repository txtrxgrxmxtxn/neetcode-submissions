class Solution: 
    def searchMatrix(self, matrix: List[List[int]], target: int)-> bool:
        if not matrix or not matrix[0]:
            return False


        m = len(matrix) #number of rows
        n = len(matrix[0]) #number of columns


        #binary search in the planned array
        left = 0
        right = m*n - 1

        while left <= right: 
            mid = (left + right) // 2

            #convert lineal index to matrix coordinates
            row = mid // n
            col = mid % n


            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target: 
                left = mid + 1
            else: 
                right = mid - 1


        return False
 

        