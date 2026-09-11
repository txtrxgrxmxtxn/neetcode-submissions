class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        used = [False] * len(nums)

        def backtrack():


            #Basis case: complete permutation
            if len(current) == len(nums):
                result.append(current[:]) #current copy
                return 


            for i in range(len(nums)):
                if not used[i]:
                    #Choose numbers.
                    used[i] = True
                    current.append(nums[i])


                    #explore:
                    backtrack()


                    #undo (backtrack)
                    current.pop()
                    used[i] = False


        backtrack()
        return result