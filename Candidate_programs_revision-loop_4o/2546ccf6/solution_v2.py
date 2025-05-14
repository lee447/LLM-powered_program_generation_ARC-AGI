from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                continue
            if i > 0 and grid[i-1][j] == 0:
                grid[i-1][j] = grid[i][j]
            if i < len(grid) - 1 and grid[i+1][j] == 0:
                grid[i+1][j] = grid[i][j]
            if j > 0 and grid[i][j-1] == 0:
                grid[i][j-1] = grid[i][j]
            if j < len(grid[i]) - 1 and grid[i][j+1] == 0:
                grid[i][j+1] = grid[i][j]
    return grid