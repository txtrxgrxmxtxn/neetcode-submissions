class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #tarea 1: inicializar estructuras.
        rows = [set() for _ in range (9)]
        cols = [set() for _ in range (9)]
        boxes = [set() for _ in range (9)]

        #tarea 2: Recorrer tablero
        for i in range(9):
            for j in range(9):
                value = board[i][j]


                #tarea 3: ignorar celdas vacias
                if value == '.':
                    continue 

                #tarea 4: Calc. indice subcuadricula
                box_index = (i// 3) * 3 + (j // 3)

                #tarea 5: Verificar duplicados
                if (value in rows[i] or 
                    value in cols[j] or
                    value in boxes[box_index]):
                    return False

                #tarea 6: Agregar a las estructuras:
                rows[i].add(value)
                cols[j].add(value)
                boxes[box_index].add(value)
        #paso 7: Retornar si es valido.

        return True
        