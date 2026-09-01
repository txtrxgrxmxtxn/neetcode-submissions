class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort() 



        def backtrack(start, current, remaining):
            if remaining == 0: 
                result.append(current[:])
                return 


            for i in range(start, len(nums)):
                #Si el numero es mayor que remaining, no puede guncionar
                if nums[i] > remaining:
                    break


                current.append(nums[i])
                backtrack(i, current, remaining - nums[i])
                current.pop()

        backtrack(0, [], target)
        return result 
        