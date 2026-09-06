# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #crear un heap vacio 
        heap = []

        #Insertar primer nodo de cada lista en el heap
        for i, lista in enumerate(lists):
            if lista: 
                #Usamos (valor, indice, nodo) para evitar comparar nodos si empate
                heapq.heappush(heap, (lista.val, i, lista))



        dummy  = ListNode(0)
        actual = dummy 


        #Mientras heap tenga elementos
        while heap: 
            #Extraer nodo con menor valor
            valor, i, nodo = heapq.heappop(heap)


            #agregar resultado
            actual.next = nodo
            actual = actual.next
        
            

            #Si nodo extraido tiene siguiente insertarlo 

            if nodo.next: 
                heapq.heappush(heap, (nodo.next.val, i, nodo.next))


        return dummy.next 
        