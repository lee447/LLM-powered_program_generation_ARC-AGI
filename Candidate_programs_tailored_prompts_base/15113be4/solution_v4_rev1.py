def solve(grid):
    H, W = len(grid), len(grid[0])
    sep_r = [r for r in range(H) if all(c==4 for c in grid[r])]
    sep_c = [c for c in range(W) if all(grid[r][c]==4 for r in range(H))]
    sep_r = [-1]+sep_r+[H]
    sep_c = [-1]+sep_c+[W]
    rows = [(sep_r[i]+1, sep_r[i+1]-1) for i in range(len(sep_r)-1)]
    cols = [(sep_c[j]+1, sep_c[j+1]-1) for j in range(len(sep_c)-1)]
    s = None
    bi = bj = dr = dc = None
    for i,(rs,re) in enumerate(rows):
        if s is not None: break
        for j,(cs,ce) in enumerate(cols):
            if s is not None: break
            for r in range(rs, re):
                if s is not None: break
                for c in range(cs, ce):
                    v = grid[r][c]
                    if v not in (0,4) and r+1<=re and c+1<=ce:
                        if grid[r][c+1]==v and grid[r+1][c]==v and grid[r+1][c+1]==v:
                            s=v; bi=i; bj=j; dr=r-rs; dc=c-cs
                            break
    out = [row[:] for row in grid]
    if s is not None:
        rs, re = rows[bi]
        for j,(cs,ce) in enumerate(cols):
            if j!=bj:
                r1, c1 = rs+dr, cs+dc
                if 0<=r1<H and 0<=c1<W and out[r1][c1]==0:
                    out[r1][c1]=s
    return out