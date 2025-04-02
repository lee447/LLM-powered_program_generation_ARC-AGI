from collections import deque
def solve(grid):
    H = len(grid)
    if H==0: 
        return grid
    W = len(grid[0])
    comp = [[None]*W for _ in range(H)]
    comps = []
    cid = 0
    for y in range(H):
        for x in range(W):
            if grid[y][x] != 0 and comp[y][x] is None:
                pts = []
                dq = deque()
                dq.append((y,x))
                comp[y][x] = cid
                while dq:
                    cy, cx = dq.popleft()
                    pts.append((cy,cx))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = cy+dy, cx+dx
                        if 0<=ny<H and 0<=nx<W:
                            if grid[ny][nx]!=0 and comp[ny][nx] is None:
                                comp[ny][nx] = cid
                                dq.append((ny,nx))
                comps.append(pts)
                cid += 1
    out = [list(row) for row in grid]
    for pts in comps:
        ys = [p[0] for p in pts]
        xs = [p[1] for p in pts]
        miny, maxy = min(ys), max(ys)
        minx, maxx = min(xs), max(xs)
        # If no interior exists, skip.
        if maxy - miny < 2 or maxx - minx < 2:
            continue
        lower_fill = None
        higher_fill = None
        # Try to get candidate from row just inside top and bottom boundaries
        ty = miny+1
        candidates = [grid[ty][x] for x in range(minx, maxx+1) if (ty,x) in pts and grid[ty][x] != 1]
        if candidates:
            lower_fill = candidates[0]
        else:
            lower_fill = 2
        by = maxy-1
        candidates = [grid[by][x] for x in range(minx, maxx+1) if (by,x) in pts and grid[by][x] != 1]
        if candidates:
            higher_fill = candidates[0]
        else:
            higher_fill = 3
        # For each interior cell of the component that is 1, change its color based on vertical position
        # Using normalized row: r = (y - miny)/(maxy - miny)
        for (y,x) in pts:
            if grid[y][x] == 1 and y!=miny and y!=maxy and x!=minx and x!=maxx:
                r = (y - miny) / (maxy - miny)
                if r < 0.5:
                    out[y][x] = lower_fill
                else:
                    out[y][x] = higher_fill
    return out