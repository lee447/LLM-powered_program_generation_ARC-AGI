def solve(grid):
    H=len(grid); W=len(grid[0])
    Bs = [(i,j) for i in range(1,H-1) if grid[i][1]!=0 and grid[i-1][1]==0]
    # locate block rows and cols
    br=[]
    for i in range(H):
        if grid[i][0]==0 and grid[i][1]!=0 and grid[i-1][1]==0: br.append(i)
    bc=[]
    for j in range(W):
        if grid[0][j]==0 and grid[1][j]!=0 and grid[0][j-1]==0: bc.append(j)
    B=5
    out=[row[:] for row in grid]
    def mask_f(bi,bj,r,c):
        if bi==0 and bj==0: return r+c<2
        if bi==0 and bj==1: return abs(c-2)>r
        if bi==0 and bj==2: return r+(4-c)<2
        if bi==1 and bj==0: return abs(r-2)+abs(c-2)<=2
        if bi==1 and bj==1: return abs(r-2)+abs(c-2)<=2
        if bi==1 and bj==2: return abs(r-2)>(4-c)
        if bi==2 and bj==0: return (4-r)+(4-c)<2
        if bi==2 and bj==1: return abs(c-2)>(4-r)
        if bi==2 and bj==2: return (4-r)+c<2
    for bi,ri in enumerate(br):
        for bj,ci in enumerate(bc):
            cnt={}
            for di in range(B):
                for dj in range(B):
                    v=grid[ri+di][ci+dj]
                    cnt[v]=cnt.get(v,0)+1
            if len(cnt)==0: continue
            mcol = min(cnt, key=cnt.get)
            Mcol = max(cnt, key=cnt.get)
            for di in range(B):
                for dj in range(B):
                    if mask_f(bi,bj,di,dj):
                        out[ri+di][ci+dj]=mcol
                    else:
                        out[ri+di][ci+dj]=Mcol
    return out