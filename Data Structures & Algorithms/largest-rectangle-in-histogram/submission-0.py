class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        pila = []
        max_area = 0 
        n = len (heights)


        for i in range(n):
            #Mientras altura actual sea menor que tope de fila 
            while pila and heights[i] < heights[pila[-1]]:
                altura = heights[pila.pop()]
                #Si pila vacia, rectangulo extenderse hasta inicio 
                anchura = i if not pila else i - pila[-1] - 1
                max_area = max(max_area, altura * anchura)
            pila.append(i)


        
        #Procesar restantes en pila
        while pila: 
            altura = heights[pila.pop()]
            anchura = n if not pila else n - pila[-1] - 1 
            max_area = max(max_area, altura*anchura)

        return max_area  