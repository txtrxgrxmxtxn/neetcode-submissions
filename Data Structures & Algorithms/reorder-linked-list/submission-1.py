# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next : 
            return

        #step 1: find the middle using slow and fast pointers:
        slow, fast = head, head
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next


        #step 2: invert second half of list
        second = slow.next
        prev= None
        slow.next = None #split list

        while second: 
            temp  = second.next 
            second.next = prev
            prev = second
            second = temp 
        
        second = prev #second is the head of second inverted list. 
        #step 3: join 2 halves
        first = head
        while second: 
            #save next nodes
            temp1 = first.next
            temp2 = second.next

            #join
            first.next = second

            #join second to temp1
            second.next = temp1

            #move pointers
            first = temp1
            second = temp2









        