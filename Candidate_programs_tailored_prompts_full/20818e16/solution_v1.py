def solve(grid):
    H, W = len(grid), len(grid[0])
    frame = grid[0][0]
    inner = [row[1:W-1] for row in grid[1:H-1]]
    h, w = len(inner), len(inner[0])
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            c = inner[i][j]
            if c != frame and not vis[i][j]:
                stack = [(i,j)]
                vis[i][j] = True
                coords = []
                while stack:
                    x,y = stack.pop()
                    coords.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not vis[nx][ny] and inner[nx][ny] == c:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                comps.append((c,coords))
    boxes = []
    for c, coords in comps:
        rs = [r for r,_ in coords]; cs = [c0 for _,c0 in coords]
        r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
        hh, ww = r1-r0+1, c1-c0+1
        mat = [[c]*ww for _ in range(hh)]
        boxes.append((hh*ww, hh, ww, mat))
    boxes.sort(key=lambda x: x[0])
    maxw = max(b[2] for b in boxes)
    totalh = sum(b[1] for b in boxes)
    out = [[frame]*maxw for _ in range(totalh)]
    r = 0
    for _, hh, ww, mat in boxes:
        for i in range(hh):
            for j in range(ww):
                out[r+i][j] = mat[i][j]
        r += hh
    return out