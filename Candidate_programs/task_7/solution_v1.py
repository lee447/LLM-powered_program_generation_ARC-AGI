def solve(grid):
    h=len(grid); w=len(grid[0])
    rows=[-1]+[i for i in range(h) if all(x==4 for x in grid[i])]+[h]
    cols=[-1]+[j for j in range(w) if all(grid[i][j]==4 for i in range(h))]+[w]
    bh=len(rows)-1; bw=len(cols)-1
    cnt={}
    for i in range(h):
        for j in range(w):
            v=grid[i][j]
            if v not in (0,1,4):
                cnt[v]=cnt.get(v,0)+1
    if cnt:
        highlight=min(cnt, key=lambda x: cnt[x])
    else:
        highlight=0
    if grid[0][2]==1:
        d=0
    else:
        d=bh//2
    out=[row[:] for row in grid]
    for bi in range(bh):
        for bj in range(bw):
            if bi+bj==d:
                r0=rows[bi]+1; c0=cols[bj]+1
                for k in (0,1):
                    if 0<=r0+k<h and 0<=c0+k<w and grid[r0+k][c0+k]==1:
                        out[r0+k][c0+k]=highlight
                    if 0<=r0+k<h and 0<=c0+2-k<w and grid[r0+k][c0+2-k]==1:
                        out[r0+k][c0+2-k]=highlight
    return out