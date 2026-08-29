class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0


        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c): 
            #Verificar limites y si es agua
            if( r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0):
                return 0 

            #Marcar como visitado
            grid[r][c] = 0


            #Contar esta celda + explorar vecinos
            area = 1 
            area += dfs(r + 1, c) #Abajo
            area += dfs(r - 1, c) #Arriba
            area += dfs(r, c + 1) #Derecha
            area += dfs(r, c - 1) #izq

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area 
        