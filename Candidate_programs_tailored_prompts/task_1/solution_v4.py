from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0]) if grid else 0
    count = 0
    for r in range(h - 1):
        for c in range(w - 1):
            if grid[r][c] == 3 and grid[r][c+1] == 3 and grid[r+1][c] == 3 and grid[r+1][c+1] == 3:
                count += 1
    count = min(count, 3)
    out = [[0]*3 for _ in range(3)]
    for i in range(count):
        out[i][i] = 1
    return out