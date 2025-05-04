def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    seeds = [(r, c) for r in range(h) for c in range(w) if grid[r][c] not in (0, 1)]
    for r, c in seeds:
        color = grid[r][c]
        c1 = c
        while c1 - 1 >= 0 and grid[r][c1 - 1] == 1:
            c1 -= 1
        c2 = c
        while c2 + 1 < w and grid[r][c2 + 1] == 1:
            c2 += 1
        r1 = r
        while r1 - 1 >= 0 and all(grid[r1 - 1][cc] == 1 for cc in range(c1, c2 + 1)):
            r1 -= 1
        r2 = r
        while r2 + 1 < h and all(grid[r2 + 1][cc] == 1 for cc in range(c1, c2 + 1)):
            r2 += 1
        if r2 - r1 >= 2 and c2 - c1 >= 2:
            for rr in range(r1 + 1, r2):
                for cc in range(c1 + 1, c2):
                    if out[rr][cc] == 1:
                        out[rr][cc] = color
    return out