from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    for c in range(w):
        rv = [(r, grid[r][c]) for r in range(h) if grid[r][c] != 0]
        if not rv: continue
        rv.sort()
        idx = 0
        for r in range(h):
            while idx < len(rv) and rv[idx][0] <= r:
                idx += 1
            if grid[r][c] == 0:
                out[r][c] = rv[idx][1] if idx < len(rv) else rv[-1][1]
    return out