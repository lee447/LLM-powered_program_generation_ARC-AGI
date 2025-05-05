from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    top = 0
    while top < h and all(grid[top][j] == bg for j in range(w)):
        top += 1
    bot = h - 1
    while bot >= 0 and all(grid[bot][j] == bg for j in range(w)):
        bot -= 1
    left = 0
    while left < w and all(grid[i][left] == bg for i in range(h)):
        left += 1
    right = w - 1
    while right >= 0 and all(grid[i][right] == bg for i in range(h)):
        right -= 1
    sub = [row[left:right+1] for row in grid[top:bot+1]]
    Hs, Ws = len(sub), len(sub[0])
    vis = [[False]*Ws for _ in range(Hs)]
    comps = []
    for i in range(Hs):
        for j in range(Ws):
            if not vis[i][j]:
                col = sub[i][j]
                q = deque([(i, j)])
                vis[i][j] = True
                cells = []
                while q:
                    y, x = q.popleft()
                    cells.append((y, x))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < Hs and 0 <= nx < Ws and not vis[ny][nx] and sub[ny][nx] == col:
                            vis[ny][nx] = True
                            q.append((ny, nx))
                ys = [y for y, x in cells]
                xs = [x for y, x in cells]
                y0, y1 = min(ys), max(ys)
                x0, x1 = min(xs), max(xs)
                hh, ww = y1-y0+1, x1-x0+1
                if len(cells) == hh*ww:
                    comps.append((y0, x0, hh, ww, col))
    comps.sort(key=lambda t: (-t[0], t[1]))
    shapes = comps
    H = max(r+h for r, c, h, w0, col in shapes)
    W = max(c+w0 for r, c, h, w0, col in shapes)
    out = [[0]*W for _ in range(H)]
    for _, c0, h0, w0, col in shapes:
        for i in range(h0):
            for j in range(w0):
                if out[i][j] == 0:
                    out[i][j] = col
    last_col = shapes[-1][4]
    for i in range(H):
        for j in range(W):
            if out[i][j] == 0:
                out[i][j] = last_col
    return out