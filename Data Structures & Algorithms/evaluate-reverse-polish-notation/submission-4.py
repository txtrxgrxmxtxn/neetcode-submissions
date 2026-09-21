from typing import List

class Solution:
    def evalRPN(self, tokens: List[int]) -> int:
        stack =[]

        for token in tokens:
            if token in "+-*/":
            #substrack last 2 numbers
                b= stack.pop() #2nd. stack
                a= stack.pop() #1st. stack


                #execute operation:
                if token == '+':
                    stack.append(a+b)
                if token == '-':
                    stack.append(a-b)
                if token == '*':
                    stack.append(a*b)
                if token == '/':
                    stack.append(int(a/b))


            else: 
                #is a number, convert to int and push
                stack.append(int(token))

        return stack[-1]

            