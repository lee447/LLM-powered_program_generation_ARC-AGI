def solve(grid):
    M=len(grid);N=len(grid[0])
    r0=M; r1=0; c0=N; c1=0
    for i in range(M):
        for j in range(N):
            if grid[i][j]==8:
                if i<r0: r0=i
                if i>r1: r1=i
                if j<c0: c0=j
                if j>c1: c1=j
    H=r1-r0+1; W=c1-c0+1
    counts={}
    for i in range(M-H+1):
        for j in range(N-W+1):
            ok=True;pat=[]
            for di in range(H):
                row=grid[i+di][j:j+W]
                for v in row:
                    if v==8:
                        ok=False;break
                if not ok:break
                pat.append(tuple(row))
            if not ok:continue
            tp=tuple(pat)
            counts[tp]=counts.get(tp,0)+1
    best=max(counts.items(),key=lambda x:x[1])[0]
    return [list(r) for r in best]