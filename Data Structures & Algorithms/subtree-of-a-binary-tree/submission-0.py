# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        #Verificar si el arbol actual coincide con subRoot
        if self.esIgual(root, subRoot):
            return True 

        #buscar en subarboles izq. y der. 

        return(
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot)
        )


    def esIgual(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
        if not p and not q:
            #Ambos none --> iguales 
            return True

        #Solo uno es None --> No iguales
        if not p or not q:
            return False 

        #Valores diferentes
        if p.val != q.val:
            return False 


        #Comparar recursivamente
        return (
            self.esIgual(p.left, q.left) and
            self.esIgual(p.right, q.right)
        )



        