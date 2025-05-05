def solve(grid):
    h, w = len(grid), len(grid[0])
    target = next((grid[r][c] for r in range(h) for c in range(w) if grid[r][c] != 0), 0)
    visited = [[False]*w for _ in range(h)]
    comps = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == target and not visited[r][c]:
                stack, pts = [(r, c)], []
                visited[r][c] = True
                while stack:
                    y, x = stack.pop()
                    pts.append((y, x))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == target:
                            visited[ny][nx] = True
                            stack.append((ny, nx))
                comps.append(pts)
    centers = [sum(x for y,x in pts)/len(pts) for pts in comps]
    order = sorted(range(len(comps)), key=lambda i: centers[i])
    if len(order) != 3:
        return grid
    left_pts = comps[order[0]]
    cen_pts  = comps[order[1]]
    right_pts= comps[order[2]]
    res = [row[:] for row in grid]
    ys = [y for y,x in cen_pts]; xs = [x for y,x in cen_pts]
    y0, y1 = min(ys), max(ys)
    x0, x1 = min(xs), max(xs)
    for r in range(y0+1, y1):
        for c in range(x0+1, x1):
            res[r][c] = 0
    ys, xs = zip(*left_pts)
    ly0, ly1 = min(ys), max(ys)
    lx0, lx1 = min(xs), max(xs)
    fillc = lx1 + 1
    for r in range(ly0+1, ly1):
        if 0 <= fillc < w:
            res[r][fillc] = target
    ys, xs = zip(*right_pts)
    ry0, ry1 = min(ys), max(ys)
    rx0, rx1 = min(xs), max(xs)
    fillc = rx0 - 1
    for r in range(ry0+1, ry1):
        if 0 <= fillc < w:
            res[r][fillc] = target
    return res