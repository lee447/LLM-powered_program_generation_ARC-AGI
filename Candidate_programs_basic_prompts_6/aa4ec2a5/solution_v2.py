def solve(grid):
    h=len(grid); w=len(grid[0])
    out=[row[:] for row in grid]
    visited=[[False]*w for _ in range(h)]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    comps=[]
    for y in range(h):
        for x in range(w):
            if grid[y][x]==1 and not visited[y][x]:
                stack=[(y,x)]; visited[y][x]=True
                pts=[]
                while stack:
                    cy,cx=stack.pop()
                    pts.append((cy,cx))
                    for dy,dx in dirs:
                        ny, nx = cy+dy, cx+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==1:
                            visited[ny][nx]=True
                            stack.append((ny,nx))
                ys=[p[0] for p in pts]; xs=[p[1] for p in pts]
                comps.append((min(ys),max(ys),min(xs),max(xs)))
    for min_y,max_y,min_x,max_x in comps:
        size = max_y-min_y+1
        if size<3: continue
        hole=False
        for yy in range(min_y+(2 if size>=5 else 1), max_y-(1 if size>=5 else 0)+1):
            for xx in range(min_x+(2 if size>=5 else 1), max_x-(1 if size>=5 else 0)+1):
                if 0<=yy<h and 0<=xx<w and grid[yy][xx]==4:
                    hole=True; break
            if hole: break
        if size>=5:
            oy0,oy1=min_y-1,max_y+1; ox0,ox1=min_x-1,max_x+1
            for xx in range(ox0,ox1+1):
                if 0<=oy0<h and 0<=xx<w: out[oy0][xx]=2
                if 0<=oy1<h and 0<=xx<w: out[oy1][xx]=2
            for yy in range(oy0,oy1+1):
                if 0<=yy<h and 0<=ox0<w: out[yy][ox0]=2
                if 0<=yy<h and 0<=ox1<w: out[yy][ox1]=2
            iy0,iy1=min_y,max_y; ix0,ix1=min_x,max_x
            for xx in range(ix0,ix1+1):
                if 0<=iy0<h and 0<=xx<w: out[iy0][xx]=8
                if 0<=iy1<h and 0<=xx<w: out[iy1][xx]=8
            for yy in range(iy0,iy1+1):
                if 0<=yy<h and 0<=ix0<w: out[yy][ix0]=8
                if 0<=yy<h and 0<=ix1<w: out[yy][ix1]=8
            fy0,fy1=min_y+1,max_y-1; fx0,fx1=min_x+1,max_x-1
            fill=6 if hole else 1
            for yy in range(fy0,fy1+1):
                for xx in range(fx0,fx1+1):
                    if 0<=yy<h and 0<=xx<w: out[yy][xx]=fill
        else:
            oy0,oy1=min_y-1,max_y+1; ox0,ox1=min_x-1,max_x+1
            for xx in range(ox0,ox1+1):
                if 0<=oy0<h and 0<=xx<w: out[oy0][xx]=2
                if 0<=oy1<h and 0<=xx<w: out[oy1][xx]=2
            for yy in range(oy0,oy1+1):
                if 0<=yy<h and 0<=ox0<w: out[yy][ox0]=2
                if 0<=yy<h and 0<=ox1<w: out[yy][ox1]=2
            fy0,fy1=min_y,max_y; fx0,fx1=min_x,max_x
            fill=6 if hole else 1
            for yy in range(fy0,fy1+1):
                for xx in range(fx0,fx1+1):
                    if 0<=yy<h and 0<=xx<w: out[yy][xx]=fill
    return out