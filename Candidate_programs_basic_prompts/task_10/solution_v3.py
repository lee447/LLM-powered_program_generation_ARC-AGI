from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    minr = min(r for r in range(h) for c in range(w) if grid[r][c] != 0)
    maxr = max(r for r in range(h) for c in range(w) if grid[r][c] != 0)
    minc = min(c for r in range(h) for c in range(w) if grid[r][c] != 0)
    maxc = max(c for r in range(h) for c in range(w) if grid[r][c] != 0)
    color = next(grid[r][c] for r in range(h) for c in range(w) if grid[r][c] != 0)
    if color in (2, 3):
        offset = 0
    elif color == 5:
        offset = 1
    else:
        offset = 3
    out = [[0] * w for _ in range(h)]
    for r in range(minr, maxr + 1):
        i = r - minr
        m = (i + offset) % 4
        if m == 1:
            d = -1
        elif m == 3:
            d = 1
        else:
            d = 0
        for c in range(minc, maxc + 1):
            if grid[r][c] != 0:
                out[r][c + d] = grid[r][c]
    return out