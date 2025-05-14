from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    result = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                if i == 0 or grid[i-1][j] == 0:
                    result[i][j] = grid[i][j]
                elif i == rows - 1 or grid[i+1][j] == 0:
                    result[i][j] = grid[i][j]
                elif j == 0 or grid[i][j-1] == 0:
                    result[i][j] = grid[i][j]
                elif j == cols - 1 or grid[i][j+1] == 0:
                    result[i][j] = grid[i][j]
                else:
                    result[i][j] = 0
            else:
                result[i][j] = 0

    return result