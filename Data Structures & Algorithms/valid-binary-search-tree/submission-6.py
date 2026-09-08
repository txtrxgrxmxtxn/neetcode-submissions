# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def es_valido(nodo: Optional[TreeNode], minimo: float, maximo: float) -> bool:
            # Nodo vacío es válido
            if not nodo:
                return True
            
            # Verificar que el valor esté en el rango permitido
            if nodo.val <= minimo or nodo.val >= maximo:
                return False
            
            # Verificar subárbol izquierdo con máximo = nodo.val
            # y subárbol derecho con mínimo = nodo.val
            return (
                es_valido(nodo.left, minimo, nodo.val) and
                es_valido(nodo.right, nodo.val, maximo)
            )
        
        return es_valido(root, float('-inf'), float('inf'))