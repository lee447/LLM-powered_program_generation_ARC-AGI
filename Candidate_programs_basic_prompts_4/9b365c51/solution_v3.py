def solve(grid):
    from collections import deque
    h, w = len(grid), len(grid[0])
    bars = []
    for x in range(w):
        cols = {grid[y][x] for y in range(h) if grid[y][x] not in (0,8)}
        if len(cols) == 1:
            bars.append((x, cols.pop()))
    bars.sort()
    bar_colors = [c for x,c in bars]
    # find components of 8
    seen = [[False]*w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            if grid[y][x]==8 and not seen[y][x]:
                q = deque([(y,x)])
                seen[y][x] = True
                pixels = []
                minx = w; maxx = 0
                while q:
                    yy, xx = q.popleft()
                    pixels.append((yy,xx))
                    minx = min(minx, xx)
                    maxx = max(maxx, xx)
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0<=ny<h and 0<=nx<w and not seen[ny][nx] and grid[ny][nx]==8:
                            seen[ny][nx] = True
                            q.append((ny,nx))
                comps.append((minx, maxx, pixels))
    # assign bar counts per comp
    B = len(bar_colors)
    C = len(comps)
    base = B//C
    rem = B % C
    # sort comps by width descending to pick rem
    widths = [(comp[1]-comp[0]+1, i) for i,comp in enumerate(comps)]
    widths.sort(reverse=True)
    k = [base]*C
    for _, i in widths[:rem]:
        k[i] += 1
    # assign bars to comps in order of ascending minx
    order = sorted(range(C), key=lambda i: comps[i][0])
    bar_ptr = 0
    comp_bars = [None]*C
    for idx in order:
        cnt = k[idx]
        comp_bars[idx] = bar_colors[bar_ptr:bar_ptr+cnt]
        bar_ptr += cnt
    # build output
    out = [[0]*w for _ in range(h)]
    for idx,(minx,maxx,pixels) in enumerate(comps):
        bs = comp_bars[idx]
        if len(bs)==1:
            for y,x in pixels:
                out[y][x] = bs[0]
        else:
            center = (minx+maxx)/2.0
            lo = bs[0]; hi = bs[-1]
            for y,x in pixels:
                out[y][x] = lo if x < center else hi
    return out