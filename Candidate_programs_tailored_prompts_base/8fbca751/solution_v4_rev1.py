def solve(grid):
    R, C = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for r in range(R-1):
        for c in range(C-1):
            a, b = grid[r][c], grid[r][c+1]
            d, e = grid[r+1][c], grid[r+1][c+1]
            vals = [a, b, d, e]
            if vals.count(8) == 3 and vals.count(0) == 1:
                idx = vals.index(0)
                dr, dc = divmod(idx, 2)
                si, sj = r + dr, c + dc
                if 0 <= si < R and 0 <= sj < C and out[si][sj] == 0:
                    out[si][sj] = 2
                if idx in (1, 3):
                    ox = -1 if dr == 0 else 1
                    oy = -1 if dc == 0 else 1
                    for dx in (0, ox):
                        for dy in (0, oy):
                            ni, nj = si + dx, sj + dy
                            if 0 <= ni < R and 0 <= nj < C and out[ni][nj] == 0:
                                out[ni][nj] = 2
    for r in range(R-1):
        for c in range(C-1):
            if grid[r][c] == 8 and grid[r+1][c] == 8 and grid[r][c+1] == 0 and grid[r+1][c+1] == 0:
                out[r][c+1] = 2
                out[r+1][c+1] = 2
    return out