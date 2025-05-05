from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    out = [[0] * (2 * w) for _ in range(2 * h)]
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0:
                orow, ocol = 2 * r, 2 * c
                out[orow][ocol] = v
                out[orow][ocol + 1] = v
                out[orow + 1][ocol] = v
                out[orow + 1][ocol + 1] = v
    return out