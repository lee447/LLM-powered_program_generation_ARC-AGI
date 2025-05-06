def solve(grid):
    h, w = len(grid), len(grid[0])
    orig = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2:
                orig.append((i,j))
    minr = min(r for r,c in orig)
    minc = min(c for r,c in orig if r==minr)
    drs = [r-minr for r,c in orig]
    dcs = [c-minc for r,c in orig]
    greens = [(i,j) for i in range(h) for j in range(w) if grid[i][j]==4]
    refg = min(greens)
    targ = min((i,j) for i in range(h) for j in range(w) if grid[i][j]==2)
    dr0 = targ[0]-refg[0]
    dc0 = targ[1]-refg[1]
    out = [row[:] for row in grid]
    for gr,gc in greens:
        for ddr, ddc in zip(drs,dcs):
            nr, nc = gr+dr0+ddr, gc+dc0+ddc
            if 0 <= nr < h and 0 <= nc < w:
                out[nr][nc] = 2
    return out