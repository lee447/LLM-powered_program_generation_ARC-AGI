def solve(grid):
    H = len(grid)
    W = len(grid[0])
    out = [row[:] for row in grid]
    for i in range(H-1):
        for j in range(W-2):
            c = 0
            for dj in range(3):
                if grid[i][j+dj] == 6: c += 1
                if grid[i+1][j+dj] == 6: c += 1
            if c >= 2:
                for di in (0,1):
                    for dj in range(3):
                        if grid[i+di][j+dj] != 6:
                            out[i+di][j+dj] = 4
    for i in range(H-2):
        for j in range(W-1):
            c = 0
            for di in range(3):
                if grid[i+di][j] == 6: c += 1
                if grid[i+di][j+1] == 6: c += 1
            if c >= 3:
                for di in range(3):
                    for dj in (0,1):
                        if grid[i+di][j+dj] != 6:
                            out[i+di][j+dj] = 4
    return out