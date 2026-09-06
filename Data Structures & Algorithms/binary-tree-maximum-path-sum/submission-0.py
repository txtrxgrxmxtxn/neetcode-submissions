# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #Variable global para guardar max sum 
        self.max_sum = float('-inf')


        def dfs(nodo: Optional[TreeNode]) -> int: 
            if not nodo:
                return 0

            #Calc. contribucion
            izq= max(0, dfs(nodo.left))
            der= max(0, dfs(nodo.right))


            #Camino que pasa por nodo
            camino = nodo.val + izq + der 

            #Actualizar suma 
            self.max_sum= max(self.max_sum, camino)

            #Retornar contribución al padre 
            return nodo.val + max(izq, der) 

        dfs(root)
        return self.max_sum 