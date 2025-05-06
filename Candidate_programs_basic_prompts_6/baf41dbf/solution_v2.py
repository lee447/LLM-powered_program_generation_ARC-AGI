def solve(grid):
    h = len(grid)
    w = len(grid[0])
    th = [(x,y) for y in range(h) for x in range(w) if grid[y][x]==3]
    bl = [(x,y) for y in range(h) for x in range(w) if grid[y][x]==6]
    xs = [x for x,y in th]; ys = [y for x,y in th]
    ox0, ox1 = min(xs), max(xs)
    oy0, oy1 = min(ys), max(ys)
    left_candidates = [x for x,y in bl if x<ox0 and oy0<=y<=oy1]
    right_candidates = [x for x,y in bl if x>ox1 and oy0<=y<=oy1]
    top_candidates = [y for x,y in bl if y<oy0 and ox0<=x<=ox1]
    bottom_candidates = [y for x,y in bl if y>oy1 and ox0<=x<=ox1]
    nx0 = max(left_candidates)+1 if left_candidates else ox0
    nx1 = min(right_candidates)-1 if right_candidates else ox1
    ny0 = max(top_candidates)+1 if top_candidates else oy0
    ny1 = min(bottom_candidates)-1 if bottom_candidates else oy1
    out = [[0]*w for _ in range(h)]
    for x,y in bl:
        out[y][x] = 6
    for x in range(nx0,nx1+1):
        if out[ny0][x]==0: out[ny0][x]=3
        if out[ny1][x]==0: out[ny1][x]=3
    for y in range(ny0,ny1+1):
        if out[y][nx0]==0: out[y][nx0]=3
        if out[y][nx1]==0: out[y][nx1]=3
    return out