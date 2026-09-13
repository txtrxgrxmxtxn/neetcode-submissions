class Solution: 
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(num : int) -> int:
            total = 0
            while num > 0: 
                digit = num % 10
                total += digit * digit
                num //= 10 

            return total



        slow = n
        fast = sumOfSquares(n)


        # Continue until they meet or fast reaches 1
        while fast != 1 and slow != fast: 
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))


        return fast == 1

        


        