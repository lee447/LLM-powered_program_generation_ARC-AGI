def solve(grid: list[list[int]]) -> list[list[int]]:
    h = len(grid)
    w = len(grid[0])
    orig = [row[:] for row in grid]
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if orig[i][j] == 1:
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < h and 0 <= nj < w and orig[ni][nj] == 0:
                            out[ni][nj] = 1
    return out