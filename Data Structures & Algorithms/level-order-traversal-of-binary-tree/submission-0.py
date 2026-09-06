# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []


        resultado = []
        cola = deque([root])


        while cola:
            nivel_actual = []
            tamano_nivel = len(cola)

            #Procesar todos los nodos del nivel actual
            for _ in range(tamano_nivel):
                nodo = cola.popleft()
                nivel_actual.append(nodo.val)

                #Agregar hijos para sig. nivel 
                if nodo.left:
                    cola.append(nodo.left)
                if nodo.right:
                    cola.append(nodo.right)

            resultado.append(nivel_actual)

        return resultado 
        