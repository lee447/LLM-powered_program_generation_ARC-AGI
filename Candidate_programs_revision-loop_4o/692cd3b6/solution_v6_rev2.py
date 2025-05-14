from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    
    def flood_fill(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or result[r][c] != 0:
            return
        result[r][c] = 4
        flood_fill(r - 1, c)
        flood_fill(r + 1, c)
        flood_fill(r, c - 1)
        flood_fill(r, c + 1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 5:
                if r > 0 and grid[r-1][c] == 2:
                    result[r][c] = 4
                if r < rows - 1 and grid[r+1][c] == 2:
                    result[r][c] = 4
                if c > 0 and grid[r][c-1] == 2:
                    result[r][c] = 4
                if c < cols - 1 and grid[r][c+1] == 2:
                    result[r][c] = 4

    for r in range(rows):
        for c in range(cols):
            if result[r][c] == 4:
                flood_fill(r, c)
    
    return result