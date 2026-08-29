# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check_height(node):
            #caso base: nodo vacio
            if not node:
                return 0

            
            #verificar sub arbol izq.
            left_height = check_height(node.left)
            if left_height == -1:
                return -1

            #verificar sub arbol der.
            right_height = check_height(node.right)
            if right_height == -1:
                return -1


            #verificar balance nodo actual
            if abs(left_height - right_height) > 1: 
                return -1

            #retornar altura nodo actual
            return 1+max(left_height, right_height)

        #Si check_height retorna -1
        return check_height(root) != -1 
        