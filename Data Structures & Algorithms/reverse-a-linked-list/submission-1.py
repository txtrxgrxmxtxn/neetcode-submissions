class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr= head

        while curr: 
            #save next temp node
            next_temp = curr.next

            #invert pointer 
            curr.next = prev

            #move prev and curr 
            prev = curr
            curr = next_temp


            #prev is new head
        return prev