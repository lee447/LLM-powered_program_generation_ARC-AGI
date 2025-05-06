def solve(grid):
    h=len(grid); w=len(grid[0])
    freq={}
    for r in grid:
        for v in r:
            if v!=0: freq[v]=freq.get(v,0)+1
    borderColor=max(freq, key=lambda k: freq[k])
    hr=[i for i in range(h) if all(grid[i][j]==borderColor for j in range(w))]
    vr=[j for j in range(w) if all(grid[i][j]==borderColor for i in range(h))]
    rs=[-1]+hr+[h]
    cs=[-1]+vr+[w]
    blocks=[]
    for bi in range(len(rs)-1):
        r0=rs[bi]+1; r1=rs[bi+1]
        row=[]
        for bj in range(len(cs)-1):
            c0=cs[bj]+1; c1=cs[bj+1]
            col0=cs[bj]+1; col1=cs[bj+1]
            col0, col1 = c0, c1
            col_found=0
            for i in range(r0, r1):
                for j in range(col0, col1):
                    v=grid[i][j]
                    if v!=0 and v!=borderColor:
                        col_found=v; break
                if col_found: break
            row.append(col_found)
        blocks.append(row)
    R=len(blocks); C=len(blocks[0]) if R>0 else 0
    if R==C: N=R-1
    else: N=min(R,C)
    diag=[blocks[i][C-1-i] for i in range(N)]
    out=[]
    for i in range(N):
        row=[diag[i] if j<=i else 0 for j in range(C)]
        out.append(row)
    return out