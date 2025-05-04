def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0:
                v = None
                for k in range(i-1, -1, -1):
                    if grid[k][j] != 0:
                        v = grid[k][j]
                        break
                if v is None:
                    for k in range(i+1, h):
                        if grid[k][j] != 0:
                            v = grid[k][j]
                            break
                out[i][j] = v if v is not None else 0
    return out