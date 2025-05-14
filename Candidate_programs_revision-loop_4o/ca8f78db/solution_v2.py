from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                grid[r][c] = grid[r-1][c]
    return grid