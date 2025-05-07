def solve(grid):
    H, W = len(grid), len(grid[0])
    from collections import deque, defaultdict
    # find colors
    cols = sorted({c for row in grid for c in row if c})
    # components by color
    comps_by_color = {}
    for c in cols:
        seen = [[False]*W for _ in range(H)]
        comps = []
        for i in range(H):
            for j in range(W):
                if grid[i][j]==c and not seen[i][j]:
                    q = deque([(i,j)])
                    seen[i][j]=True
                    comp = []
                    while q:
                        y,x = q.popleft()
                        comp.append((y,x))
                        for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                            ny,nx = y+dy, x+dx
                            if 0<=ny<H and 0<=nx<W and not seen[ny][nx] and grid[ny][nx]==c:
                                seen[ny][nx]=True
                                q.append((ny,nx))
                    ys = [y for y,x in comp]; xs = [x for y,x in comp]
                    ymin, ymax = min(ys), max(ys)
                    xmin, xmax = min(xs), max(xs)
                    mask = {(y-ymin, x-xmin) for y,x in comp}
                    comps.append((len(comp), ymin, xmin, ymax-ymin+1, xmax-xmin+1, mask))
        comps.sort(key=lambda e:e[0])
        comps_by_color[c] = comps
    # decide side for each color
    half = W/2
    side = {}
    cnt = {}
    for c in cols:
        L = sum(1 for i in range(H) for j in range(W//2) if grid[i][j]==c)
        R = sum(1 for i in range(H) for j in range(W//2, W) if grid[i][j]==c)
        side[c] = 'left' if L>R else 'right'
        cnt[c] = abs(L-R)
    if side[cols[0]]==side[cols[1]]:
        # break tie by difference
        a,b = cols
        if cnt[a]>cnt[b]:
            side[a] = 'right'
        else:
            side[b] = 'right'
    # prepare output
    out = [[0]*W for _ in range(H)]
    for c in cols:
        comps = comps_by_color[c]
        small, big = comps[0], comps[-1]
        # big
        hb, wb = big[3], big[4]
        ys_big = big[5]
        y0b = H - hb
        if side[c]=='left':
            x0b = 0
        else:
            x0b = W - wb
        for dy,dx in ys_big:
            out[y0b+dy][x0b+dx] = c
        # small
        hs, ws = small[3], small[4]
        ys_s = small[5]
        y0s = y0b - 1 - hs
        if side[c]=='left':
            x0s = 0
        else:
            x0s = W - ws
        for dy,dx in ys_s:
            out[y0s+dy][x0s+dx] = c
    return out