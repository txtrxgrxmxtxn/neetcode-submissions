from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int])-> int:
        n = len(nums)


        #phase 1: place eache value v at index v-1 (if 1 <= v < = n)
        for i in range(n):
            #while nums[i] is positive that isn't already home
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                #swap nums[i] with its correct position
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]


                #phase 2: find the first index that doesn't hold i + 1
        for i in range(n):
            if nums[i] != i+1:
                return i+1


        #all 1,..., n are present -> missing is n+1 
        return n+1