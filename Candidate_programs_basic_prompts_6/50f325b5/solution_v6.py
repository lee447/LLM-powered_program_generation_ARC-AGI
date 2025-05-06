def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(0,1),(1,0)]
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==8 and not seen[i][j]:
                stk=[(i,j)]; comp=[]
                seen[i][j]=True
                while stk:
                    x,y=stk.pop()
                    comp.append((x,y))
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==8:
                            seen[nx][ny]=True; stk.append((nx,ny))
                comps.append(comp)
    if len(comps)==1:
        comp=comps[0]
        rs=[x for x,y in comp]; cs=[y for x,y in comp]
        r0,c0=min(rs),min(cs)
        shape=[(x-r0,y-c0) for x,y in comp]
        H,W=max(x for x,y in shape)+1,max(y for x,y in shape)+1
        found=False
        for i in range(h-H+1):
            for j in range(w-W+1):
                if i<=r0-1 or i>=r0+H+1 or j<=c0-1 or j>=c0+W+1:
                    ok=True
                    for dx,dy in shape:
                        if grid[i+dx][j+dy]!=0 and grid[i+dx][j+dy]!=grid[i+dx][j+dy]:
                            ok=False;break
                    if ok:
                        for dx,dy in shape:
                            grid[i+dx][j+dy]=8
                        found=True; break
            if found: break
    else:
        for comp in comps:
            rs=[x for x,y in comp]; cs=[y for x,y in comp]
            r0,c0=min(rs),min(cs)
            shape=[(x-r0,y-c0) for x,y in comp]
            H,W=max(x for x,y in shape)+1,max(y for x,y in shape)+1
            for i in range(h-H+1):
                for j in range(w-W+1):
                    if (i,j)!=(r0,c0):
                        ok=True
                        for dx,dy in shape:
                            if grid[i+dx][j+dy]!=0:
                                ok=False;break
                        if ok:
                            for dx,dy in shape:
                                grid[i+dx][j+dy]=8
                            break
                else: continue
                break
    return grid