from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                for i in range(max(0, r-1), min(rows, r+2)):
                    for j in range(max(0, c-1), min(cols, c+2)):
                        grid[i][j] = 0
    return grid