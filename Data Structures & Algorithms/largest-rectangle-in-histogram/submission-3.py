class Solution:
    def largestRectangleArea(self, heights: List[int])-> int:

        stack = []
        max_area = 0
        n = len(heights)


        for i in range(n):

            #while actual height < top of stack
            while stack and heights[i] < heights[stack[-1]]: 
                height = heights[stack.pop()]

                #if stack is empty, the rectangle extends to start
                width = i if not stack else i - stack[-1] - 1

                max_area = max(max_area, height*width)

            stack.append(i)



        #processing rest in stack
        while stack:
            height = heights[stack.pop()]

            width = n if not stack else n - stack[-1] - 1


            max_area = max(max_area, height * width)


        return max_area 
