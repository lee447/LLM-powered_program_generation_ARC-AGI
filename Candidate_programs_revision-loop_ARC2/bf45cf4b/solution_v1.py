def solve(grid):
    bg = max({c:0 for c in []}, key=lambda k:0)
    from collections import Counter, deque
    cnt = Counter(c for row in grid for c in row)
    bg = cnt.most_common()[-1][0] if len(cnt)>1 else cnt.most_common()[0][0]
    R,C = len(grid), len(grid[0])
    regs = []
    seen = [[False]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if grid[i][j]!=bg and not seen[i][j]:
                col = grid[i][j]
                q=deque([(i,j)])
                seen[i][j]=1
                pts=[]
                while q:
                    r,c=q.popleft(); pts.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<R and 0<=nc<C and not seen[nr][nc] and grid[nr][nc]==col:
                            seen[nr][nc]=1; q.append((nr,nc))
                rs=[p[0] for p in pts]; cs=[p[1] for p in pts]
                r0,r1=min(rs),max(rs); c0,c1=min(cs),max(cs)
                full = all(grid[r][c]!=bg for r in range(r0,r1+1) for c in range(c0,c1+1))
                regs.append((full,(r1-r0+1)*(c1-c0+1),r0,r1,c0,c1))
    regs = sorted([r for r in regs if r[0]], key=lambda x:-x[1])
    if not regs:
        return grid
    _,_,r0,r1,c0,c1 = regs[0]
    h,w = r1-r0+1, c1-c0+1
    template = [row[c0:c1+1] for row in grid[r0:r1+1]]
    outR = R - h if any(all(grid[i][j]==bg for j in range(C)) for i in (0,R-1)) else R
    outC = C - w if any(all(grid[i][j]==bg for i in range(R)) for j in (0,C-1)) else C
    out = [[bg]*outC for _ in range(outR)]
    for i in range(0,outR,h):
        for j in range(0,outC,w):
            for di in range(h):
                for dj in range(w):
                    if i+di<outR and j+dj<outC:
                        out[i+di][j+dj] = template[di][dj]
    return out