
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols=len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        minutes = 0

        #step 1: collect all rotten and count fresh fruit:
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))

                elif grid[r][c] == 1:
                    fresh += 1

        #if no oranges are fresh
        if fresh == 0: 
            return 0


        directions = [(1,0),(-1, 0), (0, 1), (0, -1)]

        #step 2: Multi-source BFS:
        while queue and fresh > 0: 
            for _ in range(len(queue)): #process all oranges that rot in this min.
                r, c= queue.popleft()
                for dr, dc in directions: 
                    nr, nc = r+dr, c+dc

                    #rot the fresh neighhbor
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -=1 
                        queue.append((nr, nc))

            minutes += 1

        #step 3: if fresh oranges remain, they're unreachable
        return minutes if fresh == 0 else -1 

       