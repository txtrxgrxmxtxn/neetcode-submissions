# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Funcion invertir k nodos
        def invertir_k_nodos(primero: ListNode, k: int) -> ListNode:
            previo = None
            actual = primero 
        
            for _ in range(k): 
                siguiente = actual.next 
                actual.next = previo 
                previo = actual 
                actual = siguiente 
            
            # previo es el nuevo primero (era el k-esimo)
            return previo 



        #Nodo dummy para simplificar

        dummy = ListNode(0)
        dummy.next = head 

        previo_grupo = dummy 

        while True: 
            #Verificar si hay k nodos: 
            k_esimo = previo_grupo 
            for _ in range(k): 
                k_esimo = k_esimo.next 

                if not k_esimo:
                    return dummy.next 



            #Guarda primer nodo grupo y siguiente grupo
            primer_grupo = previo_grupo.next 
            siguiente_grupo = k_esimo.next 

            #invertir k nodos 
            nuevo_primero = invertir_k_nodos(primer_grupo, k)


            #conectar
            previo_grupo.next = nuevo_primero 
            primer_grupo.next = siguiente_grupo




            #Mover previo_grupo al ultimo nodo del grupo invertido 
            previo_grupo = primer_grupo 

        return dummy.next 
