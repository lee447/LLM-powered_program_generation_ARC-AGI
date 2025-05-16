from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2:
                cr, cc = i, j
    coords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] in (2, 3)]
    rs = [r for r, _ in coords]
    cs = [c for _, c in coords]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    up = r0 >= 2 and all(grid[r0 - 2][c] == 6 for c in range(c0, c1 + 1))
    down = r1 + 2 < h and all(grid[r1 + 2][c] == 6 for c in range(c0, c1 + 1))
    left = c0 >= 2 and all(grid[r][c0 - 2] == 6 for r in range(r0, r1 + 1))
    right = c1 + 2 < w and all(grid[r][c1 + 2] == 6 for r in range(r0, r1 + 1))
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 9 and not (r0 <= r <= r1 and c0 <= c <= c1):
                g[r][c] = 7
    if up:
        for c in range(c0, c1 + 1):
            if g[r0][c] != 2:
                g[r0][c] = 9
    if down:
        for c in range(c0, c1 + 1):
            if g[r1][c] != 2:
                g[r1][c] = 9
    if left:
        for r in range(r0, r1 + 1):
            if g[r][c0] != 2:
                g[r][c0] = 9
    if right:
        for r in range(r0, r1 + 1):
            if g[r][c1] != 2:
                g[r][c1] = 9
    return g