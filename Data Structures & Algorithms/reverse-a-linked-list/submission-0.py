# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head 

        while curr: 
            #guardar el siguiente nodo temp
            next_temp = curr.next 

            #Invertir puntero nodo actual
            curr.next = prev

            #mover prev y curr un paso
            prev = curr 
            curr = next_temp 


            #prev es nuevo head
        return prev 