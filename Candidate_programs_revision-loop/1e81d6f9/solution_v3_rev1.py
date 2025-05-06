from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bar = next(c for c in range(w) if all(grid[r][c] == 5 for r in range(h) if grid[r][c] == 5))
    cnt = {}
    for r in range(h):
        for c in range(bar+1, w):
            v = grid[r][c]
            if v != 0:
                cnt[v] = cnt.get(v, 0) + 1
    to_remove = {v for v, f in cnt.items() if f > 2}
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(bar+1, w):
            if out[r][c] in to_remove:
                out[r][c] = 0
    return out