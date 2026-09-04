class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 


        while left <= right: 
            mid = (left + right) // 2 

            #Encontrar target 
            if nums[mid] == target: 
                return mid 
            


            #Si mitad izq está ordenada
            if nums[left] <= nums[mid]:
                #Target en mitad izq. 
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                #target en mitad derecha
                else: 
                    left = mid + 1 

            #Si mitad der. está ordenada
            else: 
                #target esta mitad der. 
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 
                else: 
                    right = mid - 1 

        return -1  


