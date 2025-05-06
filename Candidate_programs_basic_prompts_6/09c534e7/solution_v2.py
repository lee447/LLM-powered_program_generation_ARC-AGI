def solve(grid):
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    changed = True
    while changed:
        changed = False
        new = [row[:] for row in g]
        for i in range(h):
            for j in range(w):
                if g[i][j] == 1:
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                        ni, nj = i + di, j + dj
                        oi, oj = i - di, j - dj
                        if 0 <= ni < h and 0 <= nj < w and 0 <= oi < h and 0 <= oj < w:
                            c = g[ni][nj]
                            if c > 1 and g[oi][oj] == c:
                                new[i][j] = c
                                changed = True
                                break
        g = new
    return g