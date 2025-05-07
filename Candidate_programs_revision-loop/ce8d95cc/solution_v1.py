def solve(grid: list[list[int]]) -> list[list[int]]:
    H=len(grid); W=len(grid[0])
    th=H//2+1
    stripes=[]
    for c in range(W):
        cnt={}
        for r in range(H):
            v=grid[r][c]
            cnt[v]=cnt.get(v,0)+1
        val,freq=max(cnt.items(), key=lambda x:x[1])
        if freq>=th and val!=0:
            stripes.append(c)
    stripes.sort()
    regs=[0]+[c+1 for c in stripes]
    if regs[-1]>=W: regs.pop()
    cols=[]
    for i,c in enumerate(stripes):
        cols.append(regs[i])
        cols.append(c)
    cols.append(regs[-1])
    r0=cols[0]
    rows=[0]
    for r in range(1,H):
        if grid[r][r0]!=grid[r-1][r0]:
            rows.append(r)
    return [[grid[r][c] for c in cols] for r in rows]