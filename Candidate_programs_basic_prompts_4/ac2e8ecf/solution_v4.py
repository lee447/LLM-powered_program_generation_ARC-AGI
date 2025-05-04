def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not vis[i][j]:
                col = grid[i][j]
                stack = [(i, j)]
                pts = []
                vis[i][j] = True
                while stack:
                    y, x = stack.pop()
                    pts.append((y, x))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < h and 0 <= nx < w and not vis[ny][nx] and grid[ny][nx] == col:
                            vis[ny][nx] = True
                            stack.append((ny, nx))
                minr = min(y for y,x in pts)
                maxr = max(y for y,x in pts)
                minc = min(x for y,x in pts)
                maxc = max(x for y,x in pts)
                sh = maxr-minr+1
                sw = maxc-minc+1
                mat = [[0]*sw for _ in range(sh)]
                for y, x in pts:
                    mat[y-minr][x-minc] = col
                shapes.append((sh*sw, col, minc, mat))
    shapes.sort(key=lambda x:(x[0], x[1], x[2]))
    out = [[0]*w for _ in range(h)]
    per = 2
    y = 0
    idx = 0
    while idx < len(shapes):
        x = 0
        rowh = 0
        for k in range(per):
            if idx+k >= len(shapes): break
            _, col, _, mat = shapes[idx+k]
            sh = len(mat)
            sw = len(mat[0])
            for dy in range(sh):
                for dx in range(sw):
                    if mat[dy][dx]:
                        out[y+dy][x+dx] = col
            x += sw + 1
            rowh = max(rowh, sh)
        idx += per
        y += rowh + 1
    return out