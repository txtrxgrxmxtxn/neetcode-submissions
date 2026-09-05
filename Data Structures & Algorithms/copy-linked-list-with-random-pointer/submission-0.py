"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        

        #Diccionario para mapear
        map = {}


        #primer recorrido: copias nodos
        actual = head
        while actual:
            map[actual] = Node(actual.val)
            actual = actual.next 


        #Segundo recorrido: punteros next y random
        actual = head 
        while actual: 
            #asignar next 
            if actual.next: 
                map[actual].next = map[actual.next]

            if actual.random:
                map[actual].random = map[actual.random]

            actual = actual.next

        return map[head]








        