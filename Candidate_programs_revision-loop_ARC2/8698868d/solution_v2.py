from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    # find connected components
    vis = [[False]*C for _ in range(R)]
    comps = []
    for i in range(R):
        for j in range(C):
            if not vis[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                vis[i][j] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<R and 0<=ny<C and not vis[nx][ny] and grid[nx][ny]==col:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                xs = [x for x,_ in cells]; ys = [y for _,y in cells]
                comps.append((col, min(xs), max(xs), min(ys), max(ys), cells))
    # background = most frequent color
    cnt = {}
    for row in grid:
        for v in row:
            cnt[v] = cnt.get(v,0)+1
    bg = max(cnt, key=lambda k: cnt[k])
    # find frame size
    sizes = []
    for col, x0,x1,y0,y1, cells in comps:
        h, w = x1-x0+1, y1-y0+1
        if col!=bg and h==w and h>2:
            sizes.append(h)
    if not sizes:
        return grid
    D = max(sizes)
    d = D-2
    # collect frames and small patterns
    frames = []
    smalls = []
    for col, x0,x1,y0,y1, cells in comps:
        h, w = x1-x0+1, y1-y0+1
        if col!=bg and h==w==D:
            frames.append((x0,y0,D,col))
        if col!=bg and h==w==d:
            smalls.append((x0,y0,d,col))
    # centers
    def center(b):
        x,y,s,_ = b
        return (x + s/2, y + s/2)
    # match each frame to nearest small by Euclid
    mapping = {}
    for f in frames:
        fx,fy,fs,fc = f
        cx,cy = center(f)
        best = None; bd = None
        for s in smalls:
            sx,sy,ss,sc = s
            c2x,c2y = center(s)
            dd = (cx-c2x)**2+(cy-c2y)**2
            if best is None or dd<bd:
                best = s; bd = dd
        if best:
            mapping[(fx,fy)] = best
    # assemble filled frames
    filled = []
    for f in frames:
        x0,y0,_,col = f
        # extract outer border
        mat = [[col]*D for _ in range(D)]
        # get small pattern
        sx,sy,_,sc = mapping.get((x0,y0),(0,0,0,0))
        pat = [[grid[i][j] for j in range(sy,sy+d)] for i in range(sx,sx+d)]
        # paste pattern into mat interior
        for i in range(d):
            for j in range(d):
                mat[i+1][j+1] = pat[i][j]
        filled.append((x0,y0,mat))
    # sort frames by top-left
    filled.sort(key=lambda x:(x[0],x[1]))
    n = int(len(filled)**0.5) if len(filled)>1 else len(filled)
    per = n
    out = []
    for bi in range(0, len(filled), per):
        rowmats = [fm[2] for fm in filled[bi:bi+per]]
        for i in range(D):
            row = []
            for m in rowmats:
                row += m[i]
            out.append(row)
    return out