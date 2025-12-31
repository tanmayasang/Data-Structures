class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c,visited):
            if r == ROWS or c == COLS or r < 0 or c < 0 or grid[r][c]=="0" or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r+1,c,visited)
            dfs(r-1,c,visited)
            dfs(r,c+1, visited)
            dfs(r,c-1,visited)
        
        res = 0
        visited = set()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row,col) not in visited:
                    dfs(row, col, visited)
                    res += 1
        return res
        
                

        
            