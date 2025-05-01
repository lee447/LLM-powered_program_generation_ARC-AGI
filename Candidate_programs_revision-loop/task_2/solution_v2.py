from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    min_r, max_r = h, -1
    min_c, max_c = w, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 8:
                if r < min_r: min_r = r
                if r > max_r: max_r = r
                if c < min_c: min_c = c
                if c > max_c: max_c = c
    H = max_r - min_r + 1
    W = max_c - min_c + 1
    out = []
    for r in range(min_r - H, min_r):
        row = []
        for c in range(min_c - W, min_c):
            row.append(grid[r][c])
        out.append(row)
    return out