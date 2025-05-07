def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if grid[i][j] == 8:
                nz = False
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if (di or dj) and grid[i+di][j+dj] != 0:
                            nz = True
                if nz:
                    for di in (-1, 0, 1):
                        for dj in (-1, 0, 1):
                            if out[i+di][j+dj] == 0:
                                if di == 0 and dj == 0:
                                    p = 8
                                elif di == 0 or dj == 0:
                                    p = 4
                                else:
                                    p = 1
                                out[i+di][j+dj] = p
    return out