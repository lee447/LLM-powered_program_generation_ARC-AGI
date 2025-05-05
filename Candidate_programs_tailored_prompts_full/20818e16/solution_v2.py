def solve(grid):
    h, w = len(grid), len(grid[0])
    # strip off uniform border
    top = 0
    while top < h and all(c == grid[top][0] for c in grid[top]):
        top += 1
    bot = h - 1
    while bot >= 0 and all(c == grid[bot][0] for c in grid[bot]):
        bot -= 1
    left = 0
    while left < w and all(grid[r][left] == grid[0][left] for r in range(h)):
        left += 1
    right = w - 1
    while right >= 0 and all(grid[r][right] == grid[0][right] for r in range(h)):
        right -= 1
    sub = [row[left:right+1] for row in grid[top:bot+1]]
    H, W = len(sub), len(sub[0])
    vis = [[False]*W for _ in range(H)]
    comps = []
    from collections import deque
    for r in range(H):
        for c in range(W):
            if not vis[r][c]:
                col = sub[r][c]
                q = deque([(r,c)])
                vis[r][c] = True
                cells = []
                while q:
                    y,x = q.popleft()
                    cells.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx = y+dy, x+dx
                        if 0<=ny<H and 0<=nx<W and not vis[ny][nx] and sub[ny][nx]==col:
                            vis[ny][nx] = True
                            q.append((ny,nx))
                ys = [y for y,x in cells]
                xs = [x for y,x in cells]
                y0,y1 = min(ys), max(ys)
                x0,x1 = min(xs), max(xs)
                area = (y1-y0+1)*(x1-x0+1)
                if len(cells)==area:
                    comps.append((y0,x0,y1-y0+1,x1-x0+1,col))
    # sort by original top descending, tie by left ascending
    comps.sort(key=lambda t:(-t[0], t[1]))
    shapes = comps[:3]
    Hs = sum(h0 for y0,x0,h0,w0,col in shapes)
    Ws = max(w0 for y0,x0,h0,w0,col in shapes)
    out = [[0]*Ws for _ in range(Hs)]
    cur = 0
    for y0,x0,hh,ww,col in shapes:
        for i in range(hh):
            for j in range(ww):
                out[cur+i][j] = col
        cur += hh
    return out