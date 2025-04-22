from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    cnt = 0
    for r in range(h - 1):
        for c in range(w - 1):
            if grid[r][c] == 3 and grid[r][c+1] == 3 and grid[r+1][c] == 3 and grid[r+1][c+1] == 3:
                cnt += 1
    out = [[0]*3 for _ in range(3)]
    for i in range(min(cnt, 3)):
        out[i][i] = 1
    return out