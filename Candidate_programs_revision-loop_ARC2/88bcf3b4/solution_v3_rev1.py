from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    # find connected components
    visited = [[False]*w for _ in range(h)]
    comps = {}
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c!=0 and not visited[y][x]:
                q = [(y,x)]
                visited[y][x]=True
                comp=[]
                for yy,xx in q:
                    comp.append((yy,xx))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx=yy+dy,xx+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==c:
                            visited[ny][nx]=True
                            q.append((ny,nx))
                comps.setdefault(c,[]).append(comp)
    # pick the axis: the component of non-background that touches top border
    axis_c = None
    axis_cells = None
    for c, lst in comps.items():
        for comp in lst:
            if any(y==0 for y,x in comp):
                axis_c = c
                axis_cells = comp
                break
        if axis_c is not None:
            break
    axis_x = axis_cells[0][1]
    axis_ys = [y for y,x in axis_cells]
    min_ay, max_ay = min(axis_ys), max(axis_ys)
    # prepare output
    out = [[0]*w for _ in range(h)]
    for y in range(min_ay, max_ay+1):
        out[y][axis_x] = axis_c
    # for each other comp do a diagonal+vertical path to axis
    for c, lst in comps.items():
        if c==axis_c: continue
        for comp in lst:
            # pick start = cell of comp with minimal y, if tie largest x
            start = min(comp, key=lambda p:(p[0], -p[1]))
            sy,sx = start
            # find target axis cell closest in Chebyshev distance
            best = None
            bd = 1e9
            for ay,ax in axis_cells:
                d = max(abs(ay-sy), abs(ax-sx))
                if d<bd:
                    bd=d; best=(ay,ax)
            ty,tx = best
            # end neighbor = diagonal neighbor of target that lies along diagonal from start
            dy = -1 if sy>ty else 1 if sy<ty else 0
            dx = -1 if sx>tx else 1 if sx<tx else 0
            ey,ex = ty+dy, tx+dx
            # chebyshev distance steps
            steps = max(abs(sy-ey), abs(sx-ex))
            for i in range(steps+1):
                yy = round(sy + (ey-sy)*i/steps)
                xx = round(sx + (ex-sx)*i/steps)
                if 0<=yy<h and 0<=xx<w:
                    out[yy][xx] = c
    return out