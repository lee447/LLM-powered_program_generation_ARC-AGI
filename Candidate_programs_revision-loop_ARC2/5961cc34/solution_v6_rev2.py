from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = next(v for row in grid for v in row if row.count(v)==h and all(r[x]==v for r in grid for x in range(w)))
    fill = next(c for row in grid for c in row if c not in (1,3,4,8))
    cols = {x for y in range(h) for x in range(w) if grid[y][x] not in (1,3,8)}
    out = [[bg]*w for _ in range(h)]
    for y in range(h):
        for x in cols:
            out[y][x] = fill
    return out