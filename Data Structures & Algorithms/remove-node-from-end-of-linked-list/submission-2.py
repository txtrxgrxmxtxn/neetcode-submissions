# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #dummy node to handle if we need to eliminate head
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy 

        #advance first n+1 positions
        for _ in range(n+1): 
            first = first.next 

        #move both pointers until first reaches the end
        while first: 
            first = first.next
            second = second.next 

        #remove node after second
        second.next = second.next.next

        return dummy.next 
        