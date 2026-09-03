class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        izquierda = 0
        derecha = len(s)-1

        while izquierda < derecha:
            s[izquierda], s[derecha] = s[derecha], s[izquierda]

            izquierda += 1
            derecha -= 1 