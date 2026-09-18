class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        p_Diag = set() # (rows + cols)
        n_Diag = set() # (rows - cols)

        res = []
        board = [["."] * n for i in range (n)]

        def backtrack(r):
            if r == n:

                copy = ["".join(row) for row in board]
                res.append(copy)
                return


            for c in range(n):
                if c in col or (r + c) in p_Diag or (r - c) in n_Diag: 
                    continue

                col.add(c)
                p_Diag.add(r+c)
                n_Diag.add(r-c)
                board[r][c]="Q"

                backtrack(r+1)

                col.remove(c)
                p_Diag.remove(r+c)
                n_Diag.remove(r-c)
                board[r][c]="."


        backtrack(0)

        return res


