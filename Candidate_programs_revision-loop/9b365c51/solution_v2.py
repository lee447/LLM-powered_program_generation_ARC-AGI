from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    stripe_x = [c for c in range(w) if grid[0][c] not in (0,8)]
    stripe_x.sort()
    stripe_cols = [grid[0][c] for c in stripe_x]
    min_s, max_s = stripe_x[0], stripe_x[-1]
    xs = [c for r in range(h) for c in range(w) if grid[r][c]==8]
    if not xs:
        return [row[:] for row in grid]
    min_c, max_c = min(xs), max(xs)
    span_s = max_s - min_s if max_s>min_s else 1
    span_c = max_c - min_c if max_c>min_c else 1
    xp = [(x-min_s)*span_c/span_s + min_c for x in stripe_x]
    thr = [(xp[i]+xp[i+1])/2 for i in range(len(xp)-1)]
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if grid[r][c]==8:
                idx = sum(c>t for t in thr)
                out[r][c] = stripe_cols[idx]
            else:
                out[r][c] = 0
    return out