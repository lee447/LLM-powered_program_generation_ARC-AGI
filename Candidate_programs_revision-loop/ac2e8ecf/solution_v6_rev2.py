def solve(grid):
    h,w=len(grid),len(grid[0])
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    vis=[[False]*w for _ in range(h)]
    rects_map={}
    others=[]
    for y in range(h):
        for x in range(w):
            if grid[y][x]!=0 and not vis[y][x]:
                col=grid[y][x]
                stack=[(y,x)]
                vis[y][x]=True
                cells=[]
                while stack:
                    cy,cx=stack.pop()
                    cells.append((cy,cx))
                    for dy,dx in dirs:
                        ny,nx=cy+dy,cx+dx
                        if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and grid[ny][nx]==col:
                            vis[ny][nx]=True
                            stack.append((ny,nx))
                ys=[cy for cy,cx in cells]
                xs=[cx for cy,cx in cells]
                y0,y1=min(ys),max(ys)
                x0,x1=min(xs),max(xs)
                hh=y1-y0+1
                ww=x1-x0+1
                cnt=len(cells)
                if cnt==hh*ww or cnt==2*(hh+ww)-4:
                    if col not in rects_map:
                        rects_map[col]=(cells,col,y0,hh,ww,x0)
                    else:
                        others.append((cells,col,y0,hh,ww,x0))
                else:
                    others.append((cells,col,y0,hh,ww,x0))
    non_grey=[]
    grey=[]
    for rect in rects_map.values():
        if rect[1]==5:
            grey.append(rect)
        else:
            non_grey.append(rect)
    non_grey.sort(key=lambda r:r[5])
    grey.sort(key=lambda r:r[5])
    hh0=max((r[3] for r in non_grey),default=0)
    hh1=max((r[3] for r in grey),default=0)
    hh_other=max((r[3] for r in others),default=0)
    out=[[0]*w for _ in range(h)]
    for cells,col,y0,hh,ww,x0 in non_grey:
        for cy,cx in cells:
            out[cy-y0][cx]=col
    for cells,col,y0,hh,ww,x0 in grey:
        for cy,cx in cells:
            out[cy-y0+hh0][cx]=col
    base=h-hh_other
    for cells,col,y0,hh,ww,x0 in others:
        for cy,cx in cells:
            out[cy-y0+base][cx]=col
    return out