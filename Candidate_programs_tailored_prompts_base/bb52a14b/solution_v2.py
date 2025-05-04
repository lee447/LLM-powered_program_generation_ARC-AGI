def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 8:
                can_fill_v = True
                if 0 <= r-1 < h and grid[r-1][c] == 1: can_fill_v = False
                if 0 <= r+1 < h and grid[r+1][c] == 1: can_fill_v = False
                for dr,dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 0:
                        if dr == 0:
                            res[nr][nc] = 4
                        elif can_fill_v:
                            res[nr][nc] = 4
    return res