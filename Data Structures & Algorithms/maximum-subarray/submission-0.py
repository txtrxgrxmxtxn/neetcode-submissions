class Solution:
    def maxSubArray(self, nums: List[int]) -> int:



        suma_actual = nums[0]
        suma_max = nums[0]



        #recorrer
        for i in range(1, len(nums)): 
            #si la suma actual es negativa empezar de nuevo
            #si no, continuar sumando
            suma_actual = max(nums[i], suma_actual + nums[i])
            #actualizar suma máx
            suma_max = max(suma_max, suma_actual)



        return suma_max 
        