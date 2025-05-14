from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                grid[i][j] = grid[i][j-1]
    return grid