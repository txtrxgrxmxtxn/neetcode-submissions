# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        actual_node = root 

        while actual_node: 
            #Si ambos son menores, ir izq.
            if p.val < actual_node.val and q.val < actual_node.val:
                actual_node = actual_node.left 
            elif p.val > actual_node.val and q.val > actual_node.val:
                actual_node = actual_node.right 


            else: 
                return actual_node

        return None #No deberia llegar si p y q están en el arbol 
        