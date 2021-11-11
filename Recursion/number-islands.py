class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def backtrack(grid, y, x): 
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid): 
                return
            
            if grid[y][x] == "1":
                grid[y][x] = "0"
                backtrack(grid, y + 1, x)
                backtrack(grid, y - 1, x)
                backtrack(grid, y, x - 1)
                backtrack(grid, y, x + 1)
        
        counter = 0
        for y_cord in range(len(grid)):
            for x_cord in range(len(grid[0])):
                if grid[y_cord][x_cord] == "1":
                    backtrack(grid, y_cord, x_cord)
                    counter += 1
        return counter
                              