class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n 



        #Dos formas para n= 1 y n=2
        prev1= 1
        prev2= 2 



        for i in range(3, n+1):
            actual = prev1+prev2
            prev1= prev2 
            prev2= actual



        return prev2