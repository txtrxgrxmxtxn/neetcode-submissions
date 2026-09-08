class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #arreglo unidimensional
        dp = [1]*n 


        #Para cada fila desde la segunda
        for i in range(1,m):
            for j in range(1,n):
                dp[j] += dp[j-1]


        return dp[n-1]