# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Variable para rastrear el diametro máximo
        self.diameter = 0 
        def height(node):
            if not node:
                return 0 


            #calcular altura sub-arbol izq y der.
            left_height = height(node.left)
            right_height = height(node.right)


            #Actualizar diametro máximo
            self.diameter = max(self.diameter, left_height + right_height)

            #retornar altura nodo Actualizar
            return 1 + max(left_height, right_height)


        height(root)
        return self.diameter
        