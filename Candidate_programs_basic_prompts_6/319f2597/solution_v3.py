def solve(grid):
    h, w = len(grid), len(grid[0])
    r = c = None
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j]==0 and grid[i][j+1]==0 and grid[i+1][j]==0 and grid[i+1][j+1]==0:
                r, c = i, j
                break
        if r is not None:
            break
    out = [row[:] for row in grid]
    br, bc = {r, r+1}, {c, c+1}
    for i in range(h):
        if i in br:
            for j in range(w):
                if grid[i][j] != 2:
                    out[i][j] = 0
        else:
            for j in bc:
                if grid[i][j] != 2:
                    out[i][j] = 0
    return out