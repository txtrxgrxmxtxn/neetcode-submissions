from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int)-> None:
        n = len(nums)
        k = k%n #normalize


        def reverse(left: int, right: int)->None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1


        #step 1: reverse whole array
        reverse(0, n-1)
        #step 2: reverse first k elem.
        reverse(0, k-1)
        #step 3: reverse remaining n-k elem.
        reverse(k, n-1)