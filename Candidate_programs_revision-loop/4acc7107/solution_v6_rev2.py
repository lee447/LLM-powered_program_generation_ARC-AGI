from collections import deque
def solve(grid):
    H, W = len(grid), len(grid[0])
    colors = sorted({c for row in grid for c in row if c != 0})
    comps_by_color = {}
    for c in colors:
        seen = [[False]*W for _ in range(H)]
        comps = []
        for i in range(H):
            for j in range(W):
                if grid[i][j] == c and not seen[i][j]:
                    q = deque([(i,j)])
                    seen[i][j] = True
                    comp = []
                    while q:
                        y, x = q.popleft()
                        comp.append((y,x))
                        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                            ny, nx = y+dy, x+dx
                            if 0 <= ny < H and 0 <= nx < W and not seen[ny][nx] and grid[ny][nx] == c:
                                seen[ny][nx] = True
                                q.append((ny,nx))
                    ys = [y for y,x in comp]
                    xs = [x for y,x in comp]
                    ymin, xmin = min(ys), min(xs)
                    h, w = max(ys)-ymin+1, max(xs)-xmin+1
                    mask = {(y-ymin, x-xmin) for y,x in comp}
                    comps.append((len(comp), ymin, xmin, h, w, mask))
        comps.sort(key=lambda e: e[0])
        comps_by_color[c] = comps
    side = {}
    for c in colors:
        L = sum(grid[i][j]==c for i in range(H) for j in range(W//2))
        R = sum(grid[i][j]==c for i in range(H) for j in range(W//2, W))
        side[c] = 'left' if L>R else 'right'
    if len(colors)>=2 and side[colors[0]] == side[colors[1]]:
        a, b = colors[0], colors[1]
        La = sum(grid[i][j]==a for i in range(H) for j in range(W//2))
        Lb = sum(grid[i][j]==b for i in range(H) for j in range(W//2))
        if La > Lb:
            side[b] = 'right'
        else:
            side[a] = 'right'
    out = [[0]*W for _ in range(H)]
    for c in colors:
        comps = comps_by_color[c]
        big = comps[-1]
        small = comps[-2] if len(comps) > 2 and comps[0][0] == 1 else comps[0]
        s0, y0s, x0s, hs, ws, ms = small
        s1, y0b, x0b, hb, wb, mb = big
        total_h = hs + hb + 1
        y0u = H - total_h
        y0l = y0u + hs + 1
        if side[c] == 'left':
            x0u = 0
            x0l = 0
        else:
            x0u = W - ws
            x0l = W - wb
        for dy, dx in ms:
            out[y0u+dy][x0u+dx] = c
        for dy, dx in mb:
            out[y0l+dy][x0l+dx] = c
    return out