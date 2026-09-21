class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int)-> List[int]:
        result = []
        dq = deque() #store index

        for i in range(len(nums)):
            #Remove elements out of window
            while dq and dq[0] < i - k +1:
                dq.popleft()


            #remove elements smaller than current one
            #because it never be the max value
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()


            #   add to actual index
            dq.append(i)

            # add result when window is complete
            if i >= k - 1:
                result.append(nums[dq[0]])


        return result

            