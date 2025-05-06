def solve(grid):
    h, w = len(grid), len(grid[0])
    color_counts = {}
    for y in range(h):
        for x in range(w):
            color_counts[grid[y][x]] = color_counts.get(grid[y][x], 0) + 1
    main_color = max(color_counts, key=color_counts.get)
    seen = [[False]*w for _ in range(h)]
    comps = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for y in range(h):
        for x in range(w):
            if grid[y][x] == main_color and not seen[y][x]:
                stack = [(y,x)]
                comp = []
                seen[y][x] = True
                while stack:
                    cy,cx = stack.pop()
                    comp.append((cy,cx))
                    for dy,dx in dirs:
                        ny,nx = cy+dy, cx+dx
                        if 0<=ny<h and 0<=nx<w and not seen[ny][nx] and grid[ny][nx]==main_color:
                            seen[ny][nx]=True
                            stack.append((ny,nx))
                comps.append(comp)
    comp = max(comps, key=len)
    ys = [p[0] for p in comp]
    xs = [p[1] for p in comp]
    y0,y1,x0,x1 = min(ys), max(ys), min(xs), max(xs)
    sub = [row[x0:x1+1] for row in grid[y0:y1+1]]
    H, W = len(sub), len(sub[0])
    out_sub = [[None]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            out_sub[i][j] = sub[j][i]
    out = [row[:] for row in grid]
    for i in range(H):
        for j in range(W):
            out[y0+i][x0+j] = out_sub[i][j]
    return out