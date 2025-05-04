def solve(grid):
    n = len(grid)
    k = n // 2
    m = k + 1
    out = [[0] * m for _ in range(m)]
    c2 = m - 1
    for i in range(m):
        for j in range(m):
            i2 = 2 * i
            j2 = 2 * j
            dx2 = i2 - c2
            dy2 = j2 - c2
            r_out2 = abs(dx2) + abs(dy2)
            r = (k * 2 - r_out2) // 2
            if dx2 == 0 and dy2 == 0:
                out[i][j] = grid[k][k]
            elif dx2 < 0 and dy2 < 0:
                out[i][j] = grid[r][r]
            elif dx2 < 0 and dy2 > 0:
                out[i][j] = grid[r][n - 1 - r]
            elif dx2 > 0 and dy2 < 0:
                out[i][j] = grid[n - 1 - r][r]
            elif dx2 > 0 and dy2 > 0:
                out[i][j] = grid[n - 1 - r][n - 1 - r]
            elif dx2 < 0 and dy2 == 0:
                out[i][j] = grid[r][r]
            elif dx2 > 0 and dy2 == 0:
                out[i][j] = grid[n - 1 - r][n - 1 - r]
            elif dx2 == 0 and dy2 < 0:
                out[i][j] = grid[r][n - 1 - r]
            elif dx2 == 0 and dy2 > 0:
                out[i][j] = grid[n - 1 - r][r]
    return out