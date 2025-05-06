def solve(grid):
    h=len(grid);w=len(grid[0])
    pts_by_color={}
    for r in range(h):
        for c in range(w):
            v=grid[r][c]
            if v>1:
                pts_by_color.setdefault(v,[]).append((r,c))
    model=max(pts_by_color.items(),key=lambda x:len(x[1]))[0]
    shape_rel=[(r-min(r for r,c in pts_by_color[model]),c-min(c for r,c in pts_by_color[model])) for r,c in pts_by_color[model]]
    orients=[]
    for swap in (False,True):
        for sx in (1,-1):
            for sy in (1,-1):
                def make(swap, sx, sy):
                    return lambda p:((p[1],p[0]) if swap else (p[0],p[1])) if False else (p[1]*sx,p[0]*sy) if swap else (p[0]*sx,p[1]*sy)
                f=make(swap,sx,sy)
                orients.append(lambda f=f: [f(p) for p in shape_rel])
    for col,pts in pts_by_color.items():
        if col==model: continue
        C=set(pts)
        for orient in orients:
            shp=orient()
            for sr,sc in shp:
                for cr,cc in C:
                    dr=cr-sr;dc=cc-sc
                    M={(r+dr,c+dc) for r,c in shp}
                    if C.issubset(M):
                        for r,c in M:
                            grid[r][c]=col
                        break
                else: continue
                break
            else: continue
            break
    return grid