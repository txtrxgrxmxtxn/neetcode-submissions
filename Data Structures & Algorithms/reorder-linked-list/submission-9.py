# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return

        #step 1: Find the mid of list using slow/fast pointers
        slow, fast = head, head
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next


        #step 2: invert second half
        second = slow.next
        slow.next = None #cut list
        prev = None

        while second: 
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev # <--- Second now is the head of second list

        #step 3: join lists.

        first = head
        while second: 
            #store next nodes
            temp1 = first.next
            temp2 = second.next

            #join 
            first.next = second 

            #connect second to temp1
            second.next = temp1
            #move pointers
            first = temp1
            second = temp2


