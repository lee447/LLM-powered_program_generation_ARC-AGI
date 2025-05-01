def solve(grid):
    h, w = len(grid), len(grid[0])
    nonzeros = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    if not nonzeros:
        return [row[:] for row in grid]
    rows = [r for r, c in nonzeros]
    min_r = min(rows)
    f = [-1, 0, 1, 0]
    out = [[0]*w for _ in range(h)]
    for r, c in nonzeros:
        d = f[(r - min_r - 1) % 4]
        nc = c + d
        out[r][nc] = grid[r][c]
    return out