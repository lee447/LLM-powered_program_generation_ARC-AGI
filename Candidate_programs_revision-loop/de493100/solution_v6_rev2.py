from collections import Counter
def solve(grid):
    n,m=len(grid),len(grid[0])
    marker=None
    for c in {x for row in grid for x in row}:
        pts=[(i,j) for i in range(n) for j in range(m) if grid[i][j]==c]
        if len(pts)>1:
            rs=[i for i,_ in pts]; cs=[j for _,j in pts]
            i0,i1,j0,j1=min(rs),max(rs),min(cs),max(cs)
            if (i1-i0+1)*(j1-j0+1)==len(pts):
                marker,(mi0,mi1,mj0,mj1)=c,(i0,i1,j0,j1)
                break
    h=mi1-mi0+1; w=mj1-mj0+1
    cnt=Counter()
    for i in range(n-h+1):
        for j in range(m-w+1):
            if not (i<mi1+1 and i+h-1>mi0-1 and j<mj1+1 and j+w-1>mj0-1):
                blk=tuple(tuple(grid[i+di][j+dj] for dj in range(w)) for di in range(h))
                cnt[blk]+=1
    blk,_=cnt.most_common(1)[0]
    return [list(r) for r in blk]