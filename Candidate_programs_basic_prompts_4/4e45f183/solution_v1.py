def solve(grid):
    R = len(grid)
    C = len(grid[0])
    rows = [i for i,row in enumerate(grid) if all(v==0 for v in row)]
    cols = [j for j in range(C) if all(grid[i][j]==0 for i in range(R))]
    br = [rows[k]+1 for k in range(len(rows)-1)]
    bc = [cols[k]+1 for k in range(len(cols)-1)]
    hs = [rows[k+1]-rows[k]-1 for k in range(len(rows)-1)]
    ws = [cols[k+1]-cols[k]-1 for k in range(len(cols)-1)]
    nb = len(hs)
    # split into blocks
    blocks = [[None]*nb for _ in range(nb)]
    for i in range(nb):
        for j in range(nb):
            h = hs[i]
            w = ws[j]
            r0 = rows[i]+1
            c0 = cols[j]+1
            b = [grid[r0 + dr][c0:c0+w] for dr in range(h)]
            blocks[i][j] = b
    # transpose mosaic
    newb = [[None]*nb for _ in range(nb)]
    for i in range(nb):
        for j in range(nb):
            newb[i][j] = [row[:] for row in blocks[j][i]]
    # reassemble
    out = [row[:] for row in grid]
    for i in range(nb):
        for j in range(nb):
            h = hs[i]
            w = ws[j]
            r0 = rows[i]+1
            c0 = cols[j]+1
            b = newb[i][j]
            for dr in range(h):
                out[r0+dr][c0:c0+w] = b[dr][:]
    return out