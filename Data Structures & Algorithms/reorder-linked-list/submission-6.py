# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode])-> None:
        if not head or not head.next: 
            return 

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = None
        slow.next = None

        while second: 
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev
        first = head
        while second: 
            temp1 = first.next
            temp2 = second.next

            first.next = second

            second.next = temp1

            first = temp1
            second = temp2



        