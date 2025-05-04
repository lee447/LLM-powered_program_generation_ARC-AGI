def solve(grid):
    H, W = len(grid), len(grid[0])
    fours = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 4]
    seen = set()
    rects = []
    for r, c in fours:
        if (r, c) in seen: continue
        stack = [(r, c)]
        comp = []
        while stack:
            y, x = stack.pop()
            if (y, x) in seen: continue
            seen.add((y, x))
            comp.append((y, x))
            for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                ny, nx = y+dy, x+dx
                if 0<=ny<H and 0<=nx<W and grid[ny][nx]==4 and (ny, nx) not in seen:
                    stack.append((ny, nx))
        ys = [y for y,x in comp]; xs = [x for y,x in comp]
        rects.append((min(ys), min(xs), max(ys), max(xs)))
    rects.sort()
    ys = sorted({y0 for y0,x0,y1,x1 in rects})
    xs = sorted({x0 for y0,x0,y1,x1 in rects})
    m = len(ys)
    n = len(xs)
    out_h = m
    out_w = 2*n + (m-1)
    out = [[0]*out_w for _ in range(out_h)]
    for i in range(m):
        for j in range(n):
            if i in (0, m-1) or j in (0, n-1):
                y = i
                x = j*2 + i
                out[y][x] = 8
    return out