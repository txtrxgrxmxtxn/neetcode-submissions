# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head


        while fast and fast.next: 
            slow = slow.next    #1 paso 
            fast = fast.next.next #avanza 2 pasos
        

            #Si se encuentran, hay ciclo
            if slow == fast:
                return True


        return False 