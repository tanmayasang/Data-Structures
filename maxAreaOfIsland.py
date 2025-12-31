class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r,c) in visited:
                return 0 
            visited.add((r,c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row,col) not in visited:
                    res = max(res, dfs(row,col))
        return res
                    