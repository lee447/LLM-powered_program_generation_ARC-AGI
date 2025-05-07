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
    diff = {}
    for c in colors:
        L = sum(grid[i][j]==c for i in range(H) for j in range(W//2))
        R = sum(grid[i][j]==c for i in range(H) for j in range(W//2, W))
        side[c] = 'left' if L>R else 'right'
        diff[c] = abs(L-R)
    if side[colors[0]] == side[colors[1]]:
        a,b = colors
        if diff[a] > diff[b]:
            side[a] = 'right'
        else:
            side[b] = 'right'
    out = [[0]*W for _ in range(H)]
    for c in colors:
        small, big = comps_by_color[c][0], comps_by_color[c][-1]
        s0, y0_0, x0_0, h0, w0, m0 = small
        s1, y0_1, x0_1, h1, w1, m1 = big
        if h0 < h1:
            upper, lower = small, big
        elif h0 > h1:
            upper, lower = big, small
        else:
            if s0 < s1:
                upper, lower = big, small
            elif s0 > s1:
                upper, lower = small, big
            else:
                if y0_0 < y0_1:
                    upper, lower = small, big
                else:
                    upper, lower = big, small
        _, _, _, hu, wu, mu = upper
        _, _, _, hl, wl, ml = lower
        total_h = hu + hl + 1
        y0u = H - total_h
        y0l = y0u + hu + 1
        if side[c] == 'left':
            x0u = 0
            x0l = 0
        else:
            x0u = W - wu
            x0l = W - wl
        for dy, dx in mu:
            out[y0u+dy][x0u+dx] = c
        for dy, dx in ml:
            out[y0l+dy][x0l+dx] = c
    return out