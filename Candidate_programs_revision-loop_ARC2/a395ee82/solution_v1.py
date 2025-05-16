def solve(grid):
    h=len(grid); w=len(grid[0])
    bg=grid[0][0]
    visited=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and grid[i][j]!=bg:
                col=grid[i][j]
                stack=[(i,j)]; pts=[]
                visited[i][j]=True
                while stack:
                    r,c=stack.pop()
                    pts.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc=r+dr,c+dc
                        if 0<=rr<h and 0<=cc<w and not visited[rr][cc] and grid[rr][cc]==col:
                            visited[rr][cc]=True
                            stack.append((rr,cc))
                comps.append((len(pts),pts,col))
    comps.sort(reverse=True,key=lambda x:x[0])
    if len(comps)<2:
        return grid
    _,a_pts,a_col=comps[0]
    _,b_pts,b_col=comps[1]
    ar=[p[0] for p in a_pts]; ac=[p[1] for p in a_pts]
    br=[p[0] for p in b_pts]; bc=[p[1] for p in b_pts]
    a_min_r,a_min_c=min(ar),min(ac)
    b_min_r,b_min_c=min(br),min(bc)
    out=[[bg]*w for _ in range(h)]
    for r,c in a_pts:
        rr=b_min_r+(r-a_min_r); cc=b_min_c+(c-a_min_c)
        if 0<=rr<h and 0<=cc<w: out[rr][cc]=a_col
    for r,c in b_pts:
        rr=a_min_r+(r-a_min_r); cc=a_min_c+(c-a_min_c)
        if 0<=rr<h and 0<=cc<w: out[rr][cc]=b_col
    return out