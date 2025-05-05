from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    d = next(c for c in range(w) if all(grid[r][c] == 4 for r in range(h)))
    L = d
    R = w - d - 1
    out_w = max(L, R)
    left = [[False] * out_w for _ in range(h)]
    right = [[False] * out_w for _ in range(h)]
    for r in range(h):
        for j in range(L):
            if grid[r][j] == 8:
                left[r][j] = True
        for j in range(R):
            if grid[r][d+1+j] == 5:
                right[r][j] = True
    res = [[2 if left[r][c] ^ right[r][c] else 0 for c in range(out_w)] for r in range(h)]
    return res