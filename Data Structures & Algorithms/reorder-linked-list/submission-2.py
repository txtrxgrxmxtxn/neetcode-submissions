# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        #Paso 1: Encontrar el medio usando slow/fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Paso 2: Invertir segunda mitad
        second = slow.next
        slow.next = None #Cortar lista
        prev = None 

        while second: 
            temp = second.next
            second.next = prev
            prev = second 
            second = temp 
        second = prev #second ahora es la cabeza de la segunda mitad invertida


        #Paso 3: Fusionar mitades
        first = head 
        while second: 
            #Guardar siguientes nodos
            temp1 = first.next 
            temp2 = second.next 

            #Conectar 
            first.next = second

            #Conectar second a temp1 
            second.next = temp1 
            #avanzar punteros
            first = temp1
            second = temp2 
            

