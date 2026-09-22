class Solution: 
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right=len(nums)-1


        while left <= right: 
            #estimate mid index
            mid = (left+right) // 2


            #verify target
            if nums[mid] == target:
                return mid

            #if target is bigger
            elif nums[mid] < target: 
                left= mid + 1

            #if target is smaller
            else:
                right = mid - 1

        #target not found
        return -1 

