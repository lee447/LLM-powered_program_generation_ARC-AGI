def solve(grid):
    h,w=len(grid),len(grid[0])
    pts=[(i,j) for i in range(h) for j in range(w) if grid[i][j]==8]
    if not pts: return []
    ys=[i for i,_ in pts]; xs=[j for _,j in pts]
    y0,y1=min(ys),max(ys); x0,x1=min(xs),max(xs)
    H=y1-y0+1; W=x1-x0+1
    full=set()
    for i in range(h-H+1):
        for j in range(w-W+1):
            ok=True
            block=[]
            for di in range(H):
                row=grid[i+di][j:j+W]
                if 8 in row:
                    ok=False; break
                block.append(tuple(row))
            if ok: full.add(tuple(block))
    cands=set(full)
    for i in range(max(0,y0-H+1),min(y1,h-H)+1):
        for j in range(max(0,x0-W+1),min(x1,w-W)+1):
            pts_block=[(i+di,j+dj) for di in range(H) for dj in range(W)]
            cnt8=sum(grid[ii][jj]==8 for ii,jj in pts_block)
            if 0<cnt8<H*W:
                known=[(di,dj,grid[i+di][j+dj]) for di in range(H) for dj in range(W) if grid[i+di][j+dj]!=8]
                new=set()
                for B in cands:
                    ok=True
                    for di,dj,v in known:
                        if B[di][dj]!=v:
                            ok=False; break
                    if ok: new.add(B)
                cands=new
        if len(cands)<=1: break
    B=cands.pop()
    return [list(r) for r in B]