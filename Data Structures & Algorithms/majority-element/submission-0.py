class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        candidate = None
        count = 0 

        for num in nums: 
            if count == 0: 
                #no active candidate: adapt current element
                candidate = num 
                count = 1

            elif num == candidate: 
                #same as candidate -> support (+1)

                count += 1

            else: 
                #different element -> (-1)
                count -= 1

        return candidate 