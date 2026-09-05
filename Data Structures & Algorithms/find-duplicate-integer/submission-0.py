class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Fase 1: encontrar punto encuentro
        tortuga = nums[0]
        liebre = nums[0]


        while True: 
            tortuga = nums[tortuga] #un paso
            liebre = nums[nums[liebre]] #dos pasos
            if tortuga == liebre:
                break 



        #fase 2: encontrar la entrada del ciclo
        tortuga = nums[0]
        while tortuga != liebre:
            tortuga = nums[tortuga]
            liebre = nums[liebre]



        return tortuga         