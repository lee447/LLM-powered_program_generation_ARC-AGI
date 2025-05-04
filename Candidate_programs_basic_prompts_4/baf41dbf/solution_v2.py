from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    coords3 = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 3]
    min_r3 = min(r for r, c in coords3)
    max_r3 = max(r for r, c in coords3)
    min_c3 = min(c for r, c in coords3)
    max_c3 = max(c for r, c in coords3)
    coords6 = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 6]
    ups = [r for r, c in coords6 if c >= min_c3 and c <= max_c3 and r < min_r3]
    top = max(ups) + 1 if ups else min_r3
    downs = [r for r, c in coords6 if c >= min_c3 and c <= max_c3 and r > max_r3]
    bottom = min(downs) - 1 if downs else max_r3
    lefts = [c for r, c in coords6 if r >= min_r3 and r <= max_r3 and c < min_c3]
    left = max(lefts) + 1 if lefts else min_c3
    rights = [c for r, c in coords6 if r >= min_r3 and r <= max_r3 and c > max_c3]
    right = min(rights) - 1 if rights else max_c3
    new = [row[:] for row in grid]
    for r, c in coords3:
        new[r][c] = 0
    for c in range(left, right+1):
        new[top][c] = 3
        new[bottom][c] = 3
    for r in range(top, bottom+1):
        new[r][left] = 3
        new[r][right] = 3
    return new