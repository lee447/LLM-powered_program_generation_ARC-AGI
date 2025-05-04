def solve(grid):
    H, W = len(grid), len(grid[0])
    for y in range(1, H):
        if grid[y] == grid[0]:
            Ty = y
            break
    for x in range(1, W):
        ok = True
        for y in range(Ty):
            if grid[y][x] != grid[y][0]:
                ok = False
                break
        if ok:
            Tx = x
            break
    base = [row[:Tx] for row in grid[:Ty]]
    res = [row[:] for row in grid]
    for y in range(H):
        for x in range(W):
            if res[y][x] == 0:
                res[y][x] = base[y % Ty][x % Tx]
    return res