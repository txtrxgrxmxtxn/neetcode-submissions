# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.contador = 0
        self.result = None 

        def inorder(nodo: Optional[TreeNode]) -> None:
            if not nodo or self.result is not None: 
                return


            #Recorrer sub-arbol izq
            inorder(nodo.left)


            #Visitar nodo actual
            self.contador += 1
            if self.contador == k: 
                self.result = nodo.val
                return


            #Recorre sub-arbol der.
            inorder(nodo.right)

        inorder(root)
        return self.result  