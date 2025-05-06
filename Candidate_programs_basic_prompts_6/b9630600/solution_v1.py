def solve(grid):
    h=len(grid); w=len(grid[0])
    # find components of 3
    seen=[[False]*w for _ in range(h)]
    comps=[]
    for y in range(h):
        for x in range(w):
            if grid[y][x]==3 and not seen[y][x]:
                stack=[(y,x)]
                seen[y][x]=True
                pts=[]
                while stack:
                    yy,xx=stack.pop()
                    pts.append((yy,xx))
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0<=ny<h and 0<=nx<w and not seen[ny][nx] and grid[ny][nx]==3:
                            seen[ny][nx]=True
                            stack.append((ny,nx))
                ys=[p[0] for p in pts]; xs=[p[1] for p in pts]
                comps.append((min(ys), max(ys), min(xs), max(xs)))
    # sort by min_y
    comps.sort(key=lambda b: b[0])
    # group by overlapping y-range
    groups=[]
    for b in comps:
        y0,y1,x0,x1=b
        if not groups or y0>groups[-1][1]:
            groups.append([y0, y1, [b]])
        else:
            groups[-1][1]=max(groups[-1][1], y1)
            groups[-1][2].append(b)
    res=[row[:] for row in grid]
    for _,_,grp in groups:
        n=len(grp)
        if n>1:
            grp.sort(key=lambda b: b[2])
            for i in range(n-1):
                y0,y1,x0,x1=grp[i]; y2,y3,x2,x3=grp[i+1]
                gap = x2 - x1 - 1
                if gap>2:
                    for r in (y0+1, y1-1):
                        for x in range(x1, x2+1):
                            if res[r][x]==0: res[r][x]=3
        else:
            y0,y1,x0,x1=grp[0]
            mid=(x0+x1)//2
            for r in (y0+1, y1-1):
                for x in range(x0, x1+1):
                    if x!=mid: res[r][x]=3
    return res