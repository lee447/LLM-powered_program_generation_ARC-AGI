def solve(grid):
    h=len(grid); w=len(grid[0])
    res=[row[:] for row in grid]
    visited=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not visited[i][j]:
                stack=[(i,j)]; visited[i][j]=True
                pts=[]
                while stack:
                    r,c=stack.pop()
                    pts.append((r,c))
                    for dr,dc in((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc=r+dr,c+dc
                        if 0<=rr<h and 0<=cc<w and not visited[rr][cc] and grid[rr][cc]==5:
                            visited[rr][cc]=True
                            stack.append((rr,cc))
                rs=[r for r,c in pts]; cs=[c for r,c in pts]
                comps.append((min(rs),max(rs),min(cs),max(cs)))
    widths=[c2-c1+1 for r1,r2,c1,c2 in comps]
    total_w = sum(widths) if len(widths)>1 else widths[0]
    for (r1,r2,c1,c2),w_u in zip(comps,widths):
        for r in range(r1+1,r2):
            for c in range(c1+1,c2):
                res[r][c]=2
    for (r1,_,c1,_),w_u in zip(comps,widths):
        start=c1
        row=r1-1
        for c in range(start,start+ (sum(widths) if len(widths)>1 else w_u)):
            if 0<=row<h and 0<=c<w and res[row][c]!=5:
                res[row][c]=2
    return res