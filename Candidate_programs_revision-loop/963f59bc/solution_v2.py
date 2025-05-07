def solve(grid):
    h=len(grid); w=len(grid[0])
    from collections import Counter
    cnt=Counter()
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=0:
                cnt[grid[r][c]]+=1
    primary=max(cnt.items(), key=lambda x:x[1])[0]
    shape=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==primary]
    sec=[(r,c,grid[r][c]) for r in range(h) for c in range(w) if grid[r][c]!=0 and grid[r][c]!=primary]
    out=[row[:] for row in grid]
    for r0,c0,col in sec:
        rows=[c for (r,c) in shape if r==r0]
        if rows:
            cs=rows
            if c0>max(cs): anchor=min(cs)
            else: anchor=max(cs)
            K=c0+anchor
            for r,c in shape:
                if r==r0 and c!=anchor: continue
                nc=K-c; nr=r
                out[nr][nc]=col
        else:
            cols=[r for (r,c) in shape if c==c0]
            if cols:
                rs=cols
                if r0>max(rs): anchor=min(rs)
                else: anchor=max(rs)
                K=r0+anchor
                for r,c in shape:
                    if c==c0 and r!=anchor: continue
                    nr=K-r; nc=c
                    out[nr][nc]=col
    return out