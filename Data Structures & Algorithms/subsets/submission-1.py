class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, current_subset):
            #agregar copia subconjunto actual
            result.append(current_subset[:])


        #explorar agregando cada elem. 
            for i in range(start, len(nums)):
                #Incluir nums[i] en el subconjunto 
                current_subset.append(nums[i])

                #Recursivamente generar subconjuntos con nums[i]
                backtrack(i+1, current_subset)


                #Backtrack: remover nums[i] para probar otras opciones
                current_subset.pop()

        backtrack(0, [])
        return result 
        