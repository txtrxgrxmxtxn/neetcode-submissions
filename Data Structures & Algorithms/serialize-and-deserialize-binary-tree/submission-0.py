# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"


        return(
            str(root.val)+","+
            self.serialize(root.left)+","+
            self.serialize(root.right)
        )

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #Convertir list. a tokens
        tokens = data.split(",")
        self.index = 0



        def build()-> Optional[TreeNode]:
            #Si no hay tokens o marcador nulo
            if self.index >= len(tokens) or tokens[self.index] == "N":
                self.index += 1
                return None 


            #Crear nodo con valor actual
            value = int(tokens[self.index])
            self.index += 1 
            nodo = TreeNode(value)



            #Construir recursivamente izq y der.
            nodo.left = build()
            nodo.right = build()


            return nodo 

        return build()














