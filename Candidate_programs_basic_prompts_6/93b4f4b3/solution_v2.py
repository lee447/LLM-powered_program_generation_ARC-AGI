def solve(grid):
    h=len(grid);w=len(grid[0]);mid=w//2;lc=mid
    bc=grid[0][0]
    out=[row[:lc] for row in grid]
    for i in range(h):
        for j in range(lc):
            if out[i][j]==0: out[i][j]=bc
    br=[i for i in range(h) if all(grid[i][j]==bc for j in range(lc))]
    segs=[]
    for k in range(len(br)-1):
        a=br[k]+1; b=br[k+1]-1
        if a<=b: segs.append((a,b))
    shapes=[]
    for a,b in segs:
        cols=[j for i in range(a,b+1) for j in range(mid,w) if grid[i][j]!=0]
        if not cols: continue
        sc=next(grid[i][j] for i in range(a,b+1) for j in range(mid,w) if grid[i][j]!=0)
        minc=min(j for i in range(a,b+1) for j in range(mid,w) if grid[i][j]==sc)
        maxc=max(j for i in range(a,b+1) for j in range(mid,w) if grid[i][j]==sc)
        W=maxc-minc+1;H=b-a+1
        mat=[[sc if grid[a+r][minc+c]==sc else 0 for c in range(W)] for r in range(H)]
        shapes.append((sc,mat))
    colors=[sc for sc,_ in shapes]
    if colors==sorted(colors):
        shapes=shapes[1:]+shapes[:1]
    elif colors==sorted(colors,reverse=True):
        shapes=list(reversed(shapes))
    for (a,b),(sc,mat) in zip(segs,shapes):
        H=len(mat);W=len(mat[0])
        pad=(lc-2-W)//2
        for r in range(H):
            for c in range(W):
                if mat[r][c]==sc:
                    out[a+r][1+pad+c]=sc
    return out