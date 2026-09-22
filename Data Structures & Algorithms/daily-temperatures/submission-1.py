class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #step 1: preparation
        result = [0] * len(temperatures)
        stack = [] #store index
        #step 2: iterate through array
        for i in range(len(temperatures)):


            #step 3: While actual temp > top value 
            while stack and temperatures[stack[-1]] < temperatures[i]:

                #step 4 estimate days:
                prev_day = stack.pop()

                result[prev_day] = i - prev_day



            #step 5: store actual day 
            stack.append(i)


        #step 6: return result
        return result
