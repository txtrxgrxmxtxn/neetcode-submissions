from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        #iterate starting last number
        for i in range(n - 1, -1, -1):
            #If is less than 9, add 1 and return

            if digits[i] < 9:
                digits[i] += 1
                return digits

            # if its 9, convert to 0 and continue
            digits[i] = 0

        return[1] + digits
        