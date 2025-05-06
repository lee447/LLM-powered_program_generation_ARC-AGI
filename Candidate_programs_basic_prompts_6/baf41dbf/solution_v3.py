from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0]) if H else 0
    coords3 = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 3]
    coords6 = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 6]
    if not coords3:
        return [row[:] for row in grid]
    minr = min(r for r, c in coords3)
    maxr = max(r for r, c in coords3)
    minc = min(c for r, c in coords3)
    maxc = max(c for r, c in coords3)
    new_minr, new_maxr = minr, maxr
    new_minc, new_maxc = minc, maxc
    left_candidates = [c for r, c in coords6 if minr <= r <= maxr and c < minc]
    if left_candidates:
        new_minc = max(left_candidates) + 1
    right_candidates = [c for r, c in coords6 if minr <= r <= maxr and c > maxc]
    if right_candidates:
        new_maxc = min(right_candidates) - 1
    up_candidates = [r for r, c in coords6 if minc <= c <= maxc and r < minr]
    if up_candidates:
        new_minr = max(up_candidates) + 1
    down_candidates = [r for r, c in coords6 if minc <= c <= maxc and r > maxr]
    if down_candidates:
        new_maxr = min(down_candidates) - 1
    out = [row[:] for row in grid]
    for r, c in coords3:
        out[r][c] = 0
    for c in range(new_minc, new_maxc + 1):
        out[new_minr][c] = 3
        out[new_maxr][c] = 3
    for r in range(new_minr, new_maxr + 1):
        out[r][new_minc] = 3
        out[r][new_maxc] = 3
    return out