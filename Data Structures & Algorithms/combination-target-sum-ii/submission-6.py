class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Ordenar para manejar duplicados
        
        def backtrack(start, current, remaining):
            # Combinación válida encontrada
            if remaining == 0:
                result.append(current[:])
                return
            
            # Suma excedida, no es válida
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Saltar duplicados en el mismo nivel
                # Esto evita combinaciones duplicadas
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Optimización: si el número excede remaining
                if candidates[i] > remaining:
                    break
                
                # Incluir el elemento actual
                current.append(candidates[i])
                
                # i+1 porque cada elemento se usa una vez
                backtrack(i + 1, current, remaining - candidates[i])
                
                # Backtrack: remover el elemento
                current.pop()
        
        backtrack(0, [], target)
        return result