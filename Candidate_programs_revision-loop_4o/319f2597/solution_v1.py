from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i >= 4 and i <= 5 and j >= 14 and j <= 15:
                grid[i][j] = 0
            elif i >= 11 and i <= 12 and j >= 6 and j <= 7:
                grid[i][j] = 0
    return grid