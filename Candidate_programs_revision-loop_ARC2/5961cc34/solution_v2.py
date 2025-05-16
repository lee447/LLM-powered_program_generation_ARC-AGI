def solve(grid):
    h, w = len(grid), len(grid[0])
    fill = None
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c not in (0,1,3,8):
                if c != 4:
                    fill = c
                elif y+1<h and grid[y+1][x] not in (0,1,3,8,4):
                    fill = grid[y+1][x]
    out = [[8]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if grid[y][x] in (1,3):
                out[y][x] = fill
    return out