# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        previous = None
        current = head

        while current: 
            #save next temp node 
            next_temp = current.next 

            #invert pointer
            current.next = previous


            #move previous and current 
            previous = current
            current = next_temp
        
        #previous is the new current
        return previous
        