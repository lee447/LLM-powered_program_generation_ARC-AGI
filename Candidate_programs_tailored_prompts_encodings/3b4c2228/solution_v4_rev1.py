from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    count = 0
    for i in range(h - 1):
        for j in range(w - 1):
            v = grid[i][j]
            if v in (2, 3) and grid[i+1][j] == v and grid[i][j+1] == v and grid[i+1][j+1] == v:
                count += 1
    n = min(count, 3)
    out = [[0]*3 for _ in range(3)]
    for k in range(n):
        out[k][k] = 1
    return out