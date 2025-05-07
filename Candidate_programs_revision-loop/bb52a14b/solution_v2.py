def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for i in range(h-2):
        for j in range(w-2):
            vals = [grid[i+di][j+dj] for di in range(3) for dj in range(3)]
            nonz = {v for v in vals if v != 0}
            if 0 in vals and nonz == {1, 8}:
                for di in range(3):
                    for dj in range(3):
                        if out[i+di][j+dj] == 0:
                            out[i+di][j+dj] = 4
    return out