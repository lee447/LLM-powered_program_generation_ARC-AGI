def solve(grid):
    h, w = len(grid), len(grid[0])
    border_color = next(c for c in grid[-1] if c != 0)
    anchor_row = h - 2
    anchors = sorted(c for c, v in enumerate(grid[anchor_row]) if v == border_color)
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for r in range(h-2):
        for c in range(w):
            if grid[r][c] != 0 and not visited[r][c]:
                col = grid[r][c]
                stack = [(r,c)]
                pts = []
                while stack:
                    y,x = stack.pop()
                    if 0 <= y < h-2 and 0 <= x < w and not visited[y][x] and grid[y][x] == col:
                        visited[y][x] = True
                        pts.append((y,x))
                        for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
                            stack.append((y+dy, x+dx))
                minr = min(y for y,x in pts)
                minc = min(x for y,x in pts)
                clusters.append((minc, pts, col))
    clusters.sort(key=lambda e: e[0])
    newg = [[0]*w for _ in range(h)]
    for x in range(w):
        newg[-1][x] = border_color
    for a in anchors:
        newg[anchor_row][a] = border_color
    for i, (_, pts, col) in enumerate(clusters):
        rel = [(y - min(y for y,x in pts), x - min(x for y,x in pts)) for y,x in pts]
        height = max(y for y,x in rel) + 1
        width = max(x for y,x in rel) + 1
        if height == 1:
            rot = [(dx, dy*0) for dy,dx in rel]
            rel = rot
            minr = min(y for y,x in rel)
            minc = min(x for y,x in rel)
            rel = [(y-minr, x-minc) for y,x in rel]
            height = max(y for y,x in rel) + 1
            width = max(x for y,x in rel) + 1
        anchor = anchors[i]
        base_x = anchor + 1
        for dy, dx in rel:
            nr = anchor_row - (height - 1) + dy
            nc = base_x + dx
            newg[nr][nc] = col
    return newg