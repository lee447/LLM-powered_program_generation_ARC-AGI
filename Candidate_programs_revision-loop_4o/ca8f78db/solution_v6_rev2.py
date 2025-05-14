from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    for r in range(2, len(grid), 2):
        for c in range(len(grid[0])):
            grid[r][c] = grid[r-1][c]
    return grid