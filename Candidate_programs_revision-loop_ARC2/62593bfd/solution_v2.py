def solve(grid):
    H, W = len(grid), len(grid[0])
    bg = max({c:grid_row.count(c) for grid_row in grid for c in grid_row}, key=lambda x: sum(row.count(x) for row in grid))
    visited = [[False]*W for _ in range(H)]
    clusters = []
    for i in range(H):
        for j in range(W):
            if grid[i][j]!=bg and not visited[i][j]:
                col=grid[i][j]
                stack=[(i,j)]
                pts=[]
                visited[i][j]=True
                while stack:
                    r,c=stack.pop()
                    pts.append((r,c))
                    for dr,dc in((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc=r+dr,c+dc
                        if 0<=rr<H and 0<=cc<W and not visited[rr][cc] and grid[rr][cc]==col:
                            visited[rr][cc]=True
                            stack.append((rr,cc))
                rs=[p[0]for p in pts]; cs=[p[1]for p in pts]
                clusters.append((min(rs),min(cs),col,pts))
    clusters.sort(key=lambda x:(x[0],x[1]))
    # choose half for top
    # find how many fit in top by greedy width
    tops=[]; bots=[]
    x=0
    for mnr,mnc,col,pts in clusters:
        ws = max(c for r,c in pts) - mnc + 1
        if x+ws<=W:
            tops.append((mnr,mnc,col,pts))
            x+=ws+1
        else:
            bots.append((mnr,mnc,col,pts))
    # prepare output
    out=[[bg]*W for _ in range(H)]
    def place(group, row0):
        x=0
        for mnr,mnc,col,pts in group:
            pts_sorted = sorted(pts)
            rs=[r for r,c in pts]; cs=[c for r,c in pts]
            h = max(rs)-mnr
            for r,c in pts:
                nr = row0 + (r-mnr)
                nc = x + (c-mnc)
                out[nr][nc]=col
            x += (max(cs)-mnc+1)+1
    place(tops,0)
    place(bots,H-max(p[0] for p in bots)-1)
    return out