def solve(grid):
    H = len(grid)
    W = len(grid[0])
    minr, maxr = H, -1
    minc, maxc = W, -1
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 8:
                if r < minr: minr = r
                if r > maxr: maxr = r
                if c < minc: minc = c
                if c > maxc: maxc = c
    h = maxr - minr + 1
    w = maxc - minc + 1
    left = minc - w
    out = []
    for r in range(minr, maxr+1):
        row = []
        for c in range(left, minc):
            row.append(grid[r][c])
        out.append(row)
    return out