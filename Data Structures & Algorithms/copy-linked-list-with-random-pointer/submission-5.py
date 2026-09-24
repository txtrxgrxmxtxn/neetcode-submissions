"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution: 
    def copyRandomList(self, head: 'Optional[List]') -> 'Optional[List]':

        if not head:
            return      

        #hash map
        map = {}
        
        #first iteration: copy the nodes

        actual = head
        while actual: 
            map[actual] = Node(actual.val) #store node values
            actual = actual.next

        #second iteration: next and random pointers
        actual = head
        while actual: 
            #assign next
            if actual.next: 
                map[actual].next = map[actual.next]


            if actual.random: 
                map[actual].random = map[actual.random]

            actual = actual.next

        return map[head]












        