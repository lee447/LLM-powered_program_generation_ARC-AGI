def solve(grid):
    from collections import deque, Counter
    H, W = len(grid), len(grid[0])
    # detect background color as most common on the border
    border = []
    for x in range(W):
        border.append(grid[0][x]); border.append(grid[H-1][x])
    for y in range(1, H-1):
        border.append(grid[y][0]); border.append(grid[y][W-1])
    bg = Counter(border).most_common(1)[0][0]
    seen = [[False]*W for _ in range(H)]
    rects = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] != bg and not seen[i][j]:
                col = grid[i][j]
                q = deque([(i,j)])
                seen[i][j] = True
                cells = [(i,j)]
                while q:
                    y,x = q.popleft()
                    for dy,dx in dirs:
                        ny, nx = y+dy, x+dx
                        if 0<=ny<H and 0<=nx<W and not seen[ny][nx] and grid[ny][nx]==col:
                            seen[ny][nx] = True
                            q.append((ny,nx))
                            cells.append((ny,nx))
                rs = [r for r,c in cells]; cs = [c for r,c in cells]
                minr, maxr = min(rs), max(rs)
                minc, maxc = min(cs), max(cs)
                sub = [row[minc:maxc+1] for row in grid[minr:maxr+1]]
                h = maxr-minr+1; w = maxc-minc+1
                rects.append((h*w, h, w, sub))
    rects.sort(key=lambda x: x[0])
    if not rects:
        return grid
    # new canvas size
    heights = [h for area,h,w,sub in rects]
    widths = [w for area,h,w,sub in rects]
    H2 = max(heights)
    W2 = sum(widths)
    canvas = [[bg]*W2 for _ in range(H2)]
    xoff = 0
    for area,h,w,sub in rects:
        for y in range(h):
            for x in range(w):
                canvas[y][xoff+x] = sub[y][x]
        xoff += w
    return canvas