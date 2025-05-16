def solve(grid):
    h, w = len(grid), len(grid[0])
    fill = next(c for row in grid for c in row if c not in (1,3,4,8))
    out = [[8]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if grid[y][x] in (1,3):
                out[y][x] = fill
    return out