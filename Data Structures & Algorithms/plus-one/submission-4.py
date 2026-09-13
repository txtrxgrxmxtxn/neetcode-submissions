from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Recorrer desde el último dígito
        for i in range(n - 1, -1, -1):
            # Si es menor que 9, sumar 1 y retornar
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Si es 9, convertirlo en 0 y continuar (acarreo)
            digits[i] = 0
        
        # Si llegamos aquí, todos eran 9
        return [1] + digits