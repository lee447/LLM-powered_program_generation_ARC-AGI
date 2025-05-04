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
                if idx == 3:
                    si, sj, ox, oy = r+1, c+1, 1, 1
                elif idx == 2:
                    si, sj, ox, oy = r+1, c, 1, -1
                elif idx == 1:
                    si, sj, ox, oy = r, c+1, -1, 1
                else:
                    si, sj, ox, oy = r, c, -1, -1
                for dx in (0, ox):
                    for dy in (0, oy):
                        ni, nj = si+dx, sj+dy
                        if 0 <= ni < R and 0 <= nj < C and out[ni][nj] == 0:
                            out[ni][nj] = 2
    return out