def solve(grid):
    R = len(grid)
    C = len(grid[0]) if R else 0
    secs = []
    for i in range(R-1):
        bs = []
        for j in range(C-1):
            if grid[i][j]==8 and grid[i][j+1]==8 and grid[i+1][j]==8 and grid[i+1][j+1]==8:
                bs.append(j)
        if len(bs)==2:
            secs.append((i, bs[0], bs[1]))
    out = []
    for i, j, k in secs:
        cols = list(range(j+2, k))
        for r in (i, i+1):
            out.append([grid[r][c] if grid[r][c]!=8 else 0 for c in cols])
    return out