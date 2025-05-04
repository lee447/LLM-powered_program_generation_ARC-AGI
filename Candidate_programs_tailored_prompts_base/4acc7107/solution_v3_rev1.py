import collections
def solve(grid):
    h,w=len(grid),len(grid[0])
    vis=[[False]*w for _ in range(h)]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    clusters_by_color={}
    for i in range(h):
        for j in range(w):
            c=grid[i][j]
            if c>0 and not vis[i][j]:
                q=[(i,j)]
                vis[i][j]=True
                cells=[]
                while q:
                    x,y=q.pop()
                    cells.append((x,y))
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==c:
                            vis[nx][ny]=True
                            q.append((nx,ny))
                clusters_by_color.setdefault(c,[]).append(cells)
    info={}
    for c,clists in clusters_by_color.items():
        clists.sort(key=len)
        small,large=clists[0],clists[1]
        sr,sc=min(r for r,_ in small),min(c0 for _,c0 in small)
        lr,lc=min(r for r,_ in large),min(c0 for _,c0 in large)
        small_rel=[(r-sr,c0-sc) for r,c0 in small]
        large_rel=[(r-lr,c0-lc) for r,c0 in large]
        sh,sw=max(r for r,c0 in small_rel)+1,max(c0 for r,c0 in small_rel)+1
        lh,lw=max(r for r,c0 in large_rel)+1,max(c0 for r,c0 in large_rel)+1
        info[c]=(small_rel,sh,sw,large_rel,lh,lw)
    sorted_colors=sorted(info.keys(),key=lambda c:(len(info[c][0]),len(info[c][3])))
    block1_h=max(v[1] for v in info.values())
    block2_h=max(v[4] for v in info.values())
    vg=1;hg=1
    row2=h-block2_h
    row1=row2-vg-block1_h
    out=[[0]*w for _ in range(h)]
    x=0
    for c in sorted_colors:
        small_rel,sh,sw,large_rel,lh,lw=info[c]
        for dr,dc in small_rel:
            out[row1+dr][x+dc]=c
        for dr,dc in large_rel:
            out[row2+dr][x+dc]=c
        x+=lw+hg
    return out