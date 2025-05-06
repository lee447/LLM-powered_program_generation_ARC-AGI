def solve(grid):
    H, W = len(grid), len(grid[0])
    # find the contiguous block of color 3
    pts3 = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == 3]
    mi, Ma = min(x for x, y in pts3), max(x for x, y in pts3)
    mj, MB = min(y for x, y in pts3), max(y for x, y in pts3)
    h, w = Ma - mi + 1, MB - mj + 1
    # choose whether to sample above or below the 3‐block
    if mi > 0:
        base = mi - 1
        out = [[grid[base + di][mj + dj] for dj in range(w)] for di in range(h)]
    else:
        base = Ma + 1
        out = [[grid[base - di][mj + dj] for dj in range(w)] for di in range(h)]
    return out