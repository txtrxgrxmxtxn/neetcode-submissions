# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node: Optional[TreeNode], maximo: int) -> int:
            if not node:
                return 0

            count = 0 


            #Si nodo actual es mayor o igual
            if node.val >= maximo:
                count = 1 
                maximo = node.val 


            #Continuar con hijos
            count += dfs(node.left, maximo)
            count += dfs(node.right, maximo)


            return count

        return dfs(root, float('-inf')) 
