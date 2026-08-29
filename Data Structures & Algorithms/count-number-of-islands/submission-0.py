class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            #verificar limites y si es agua
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or 
                grid[r][c] == '0'):
                return 

            #Marcar como visitado (convertir a agua)
            grid[r][c] = '0'


            #Explorar 4 direcciones
            dfs(r+1, c) #Abajo
            dfs(r-1, c) #Arriba
            dfs(r, c+1) #Derecha
            dfs(r, c-1) #izq

        #recorrer cuadricula
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r,c) #explorar y marcar numIslands
        
        return count 
        