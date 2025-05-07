def solve(grid):
    H=len(grid);W=len(grid[0])
    horiz=True
    for j in range(W):
        if grid[0][j]!=grid[0][0]:
            horiz=False;break
    stripes=[]
    if horiz:
        bg=[]
        for r in range(H):
            br=None
            for c in range(W):
                if grid[r][c]!=2:
                    br=grid[r][c];break
            bg.append(br)
        r0=0;cur=bg[0]
        for r in range(1,H):
            if bg[r]!=cur:
                stripes.append((r0,r-1,cur));r0=r;cur=bg[r]
        stripes.append((r0,H-1,cur))
    else:
        bgc=[]
        for c in range(W):
            bc=None
            for r in range(H):
                if grid[r][c]!=2:
                    bc=grid[r][c];break
            bgc.append(bc)
        c0=0;cur=bgc[0]
        for c in range(1,W):
            if bgc[c]!=cur:
                stripes.append((c0,c-1,cur));c0=c;cur=bgc[c]
        stripes.append((c0,W-1,cur))
    out=[row[:] for row in grid]
    visited=[[False]*W for _ in range(H)]
    for stripe in stripes:
        if horiz:
            r_start,r_end,bgcolor=stripe; c_start,c_end=0,W-1
        else:
            c_start,c_end,bgcolor=stripe; r_start,r_end=0,H-1
        for r in range(r_start,r_end+1):
            for c in range(c_start,c_end+1):
                if grid[r][c]==2 and not visited[r][c]:
                    stack=[(r,c)];visited[r][c]=True;comp=[]
                    while stack:
                        x,y=stack.pop();comp.append((x,y))
                        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx,ny=x+dx,y+dy
                            if 0<=nx<H and 0<=ny<W and r_start<=nx<=r_end and c_start<=ny<=c_end and not visited[nx][ny] and grid[nx][ny]==2:
                                visited[nx][ny]=True;stack.append((nx,ny))
                    rs=[x for x,y in comp];cs=[y for x,y in comp]
                    rmin,rmax=min(rs),max(rs);cmin,cmax=min(cs),max(cs)
                    w=cmax-cmin+1
                    for x,y in comp: out[x][y]=bgcolor
                    if bgcolor==1:
                        new_c2=c_end;new_c1=new_c2-(w-1)
                    else:
                        new_c1=c_start;new_c2=new_c1+(w-1)
                    for rr in range(rmin,rmax+1):
                        for cc in range(new_c1,new_c2+1):
                            out[rr][cc]=2
    return out