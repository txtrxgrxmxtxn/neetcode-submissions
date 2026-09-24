# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution: 
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode])-> Optional[ListNode]:
        
        #Dummy node to use and simplify the iteration process
        dummy = ListNode(0)
        actual = dummy
        carry = 0 

        while l1 or l2 or carry: 

            #get actual values:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # add them up
            addition = val1 + val2 + carry

            #estimate new digit and carry
            digit = addition % 10 #stores the digits 
            carry = addition // 10 #stores carried values

            actual.next = ListNode(digit)
            actual = actual.next


            #advance iteration
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next

        return dummy.next 



        