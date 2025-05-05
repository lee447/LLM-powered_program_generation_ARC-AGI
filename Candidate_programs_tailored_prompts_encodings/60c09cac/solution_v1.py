from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    out = [[0] * (2 * w) for _ in range(2 * h)]
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0:
                rr = 2 * r
                cc = 2 * c
                out[rr][cc] = v
                out[rr][cc + 1] = v
                out[rr + 1][cc] = v
                out[rr + 1][cc + 1] = v
    return out