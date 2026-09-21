class Solution:
    def isValid(self, s: str) -> bool: 
        #stack to keep the following opened parenthesis
        stack = []


        #map closed parenthesis.
        bracket_map = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for char in s: 
            #if there's closed parenth.
            if char in bracket_map:
                #remove and return last element of stack
                #if stack is empty, return '#'

                top_element = stack.pop() if stack else '#'

                if bracket_map[char] != top_element:
                    return False


            else:
                stack.append(char)


        return not stack 