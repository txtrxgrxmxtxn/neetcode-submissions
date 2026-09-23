class Solution:
    def findDuplicate(self, nums: List[int])-> int:
        #step 1: find matching point: 
        turtle = nums[0]
        rabbit = nums[0]


        while True: 
            turtle = nums[turtle] #1 step
            rabbit = nums[nums[rabbit]] #2 steps
            if turtle == rabbit: 
                break


        #step 2: find cycle entrance
        turtle = nums[0]
        while turtle != rabbit: 
            turtle = nums[turtle]
            rabbit = nums[rabbit]

        return turtle