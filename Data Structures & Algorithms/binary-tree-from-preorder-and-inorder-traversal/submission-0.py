# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {value: idx for idx, value in enumerate(inorder)}

        def build(pre_left: int, pre_right: int, in_left: int, in_right: int) -> Optional[TreeNode]:

            #Caso base: No hay elementos
            if pre_left > pre_right or in_left > in_right:
                return None


            #El primer elem. de preorder es la raiz
            root_val = preorder[pre_left]
            root = TreeNode(root_val)


            #Encontrer posicion de la raiz en inorder
            root_idx = inorder_index[root_val]

            #tamaño del subarbol izq 
            left_size = root_idx - in_left 

            #Construir sub-arbol izq. 
            root.left = build (
                pre_left + 1,                   #inicio subarbol izq en preorder
                pre_left + left_size,           #fin subarbol izq en preorder
                in_left,                        #inicio del subarbol izq en inorder 
                root_idx - 1                    #fin subarbol izq inorder 
            )


            #Construir sub-arbol der. 

            root.right = build(

                pre_left + left_size + 1,        #inicio subarbol der. en preorder 
                pre_right,                      #fin sub arbol der. en preorder
                root_idx + 1,                   #Inicio subarbol der. inorder
                in_right                        #fin subarbol der. inorder
            )


            return root 


        return build(0, len(preorder)-1, 0, len(inorder) - 1)














        