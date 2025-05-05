def solve(grid):
    H, W = len(grid), len(grid[0])
    ax = ay = None
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 2:
                ax, ay = i, j
                break
        if ax is not None:
            break
    out = [row[:] for row in grid]
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v in (1, 3):
                if c-1 >= 0 and c+1 < W and grid[r][c-1] == v and grid[r][c+1] == v:
                    d = (ax > r) - (ax < r)
                    for m in (-1, 0, 1):
                        rr = r + d*m
                        cc = c
                        if 0 <= rr < H and 0 <= cc < W and grid[rr][cc] == 0:
                            out[rr][cc] = 2
                if r-1 >= 0 and r+1 < H and grid[r-1][c] == v and grid[r+1][c] == v:
                    d = (ay > c) - (ay < c)
                    for m in (-1, 0, 1):
                        rr = r
                        cc = c + d*m
                        if 0 <= rr < H and 0 <= cc < W and grid[rr][cc] == 0:
                            out[rr][cc] = 2
    return out