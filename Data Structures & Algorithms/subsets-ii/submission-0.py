from typing import List

class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Sort to group duplicates
        nums.sort()

        result = []
        current = []

        def backtrack(start: int) -> None:
            # add the actual subset

            result.append(current[:])


            for i in range(start, len(nums)):
                #Skip duplicates 

                if i > start and nums[i] == nums[i - 1]:
                    continue

                #choose nums[i]
                current.append(nums[i])

                #explore 
                backtrack(i + 1)

                #undo (backtrack)
                current.pop()


        backtrack(0)
        return result 

        