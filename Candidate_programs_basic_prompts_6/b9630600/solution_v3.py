def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    changed = True
    while changed:
        changed = False
        new = [row[:] for row in res]
        for r in range(1, h-1):
            for c in range(1, w-1):
                if res[r][c] == 0:
                    if res[r][c-1] == 3 and res[r][c+1] == 3:
                        new[r][c] = 3
                        changed = True
                    elif res[r-1][c] == 3 and res[r+1][c] == 3:
                        new[r][c] = 3
                        changed = True
        res = new
    return res