class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            medio = (right + left) // 2


            if nums[medio] > nums[right]:
                left = medio + 1

            else: 
                right = medio


        return nums[left ]

        