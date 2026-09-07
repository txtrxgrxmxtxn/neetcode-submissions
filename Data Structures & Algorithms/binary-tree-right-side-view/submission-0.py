# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []


        result = []
        tail = deque([root])


        while tail: 
            size = len(tail)

            for i in range(size):

                node = tail.popleft()

                #agregar hijos a cola
                if node.left:
                    tail.append(node.left)
                if node.right:
                    tail.append(node.right)

                #Si es ultimo nodo de nivel ---> Visible

                if i == size - 1:
                    result.append(node.val)


        return result 

        