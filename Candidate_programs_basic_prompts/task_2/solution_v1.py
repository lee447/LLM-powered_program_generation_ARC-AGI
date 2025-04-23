def solve(grid):
    h, w = len(grid), len(grid[0])
    minr, maxr = h, -1
    minc, maxc = w, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 8:
                if r < minr: minr = r
                if r > maxr: maxr = r
                if c < minc: minc = c
                if c > maxc: maxc = c
    ch = maxr - minr + 1
    cw = maxc - minc + 1
    out = []
    for i in range(ch):
        row = []
        sr = minr - ch + i
        sc = minc
        for j in range(cw):
            row.append(grid[sr][sc + j])
        out.append(row)
    return out