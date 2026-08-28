# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0 
        
        #depth del sub-arbol izq.
        left_depth = self.maxDepth(root.left)

        #depth del sub-arbol der.
        right_depth= self.maxDepth(root.right)

        #Retornar 1 (nodo actual) + la profundidad máxima de los sub-arboles
        return 1+max(left_depth, right_depth)