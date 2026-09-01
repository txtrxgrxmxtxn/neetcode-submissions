# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Nodo dummy para manejar el caso de eliminar el head 
        dummy = ListNode(0)
        dummy.next = head


        first = dummy 
        second = dummy 

        #avanzar first n+1 posiciones
        for _ in range(n+1): 
            first = first.next 

        #Mover ambos punteros hasta que first llegue al final
        while first:
            first = first.next
            second = second.next 


        #Eliminar nodo despues de second 
        second.next = second.next.next 

        return dummy.next 