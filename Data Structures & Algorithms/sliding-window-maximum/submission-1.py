class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [] 
        dq = deque() #Almacenar indices


        for i in range(len(nums)):
            #Remover elementos fuera de ventana
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            #remover elem. más pequeños q el actual
            # nunca serán el máximo
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()


            #agregar indice actual
            dq.append(i)


            #agregar resultado cuando la ventana está completa

            if i >= k-1:
                result.append(nums[dq[0]])

        return result 


