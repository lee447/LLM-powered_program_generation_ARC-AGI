def solve(grid):
    H=len(grid);W=len(grid[0])
    bottom=grid[-1]
    bc=next((v for v in bottom if v!=0),0)
    ar=H-2
    anchors=[c for c in range(W) if grid[ar][c]==bc]
    vis=[[False]*W for _ in range(H)]
    clusters=[]
    for r in range(ar):
        for c in range(W):
            if not vis[r][c] and grid[r][c]!=0:
                col=grid[r][c]
                q=[(r,c)];vis[r][c]=True;cells=[(r,c)]
                for rr,cc in q:
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0<=nr<ar and 0<=nc<W and not vis[nr][nc] and grid[nr][nc]==col:
                            vis[nr][nc]=True
                            q.append((nr,nc));cells.append((nr,nc))
                area=len(cells)
                new_w=area//2
                clusters.append((area,new_w,col))
    clusters.sort(key=lambda x:x[0])
    res=[[0]*W for _ in range(H)]
    res[-1]=bottom.copy()
    for x in anchors: res[ar][x]=bc
    for _,w,col in clusters:
        for x in anchors:
            s=x+1; e=s+w
            if e<=W and all(res[ar][j]==0 for j in range(s,e)):
                for j in range(s,e):
                    res[ar][j]=col;res[ar-1][j]=col
                break
    return res