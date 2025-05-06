def solve(grid):
    from collections import deque
    H, W = len(grid), len(grid[0])
    colors = sorted({c for row in grid for c in row if c != 0})
    def find_comps(c):
        seen = [[False]*W for _ in range(H)]
        comps = []
        for i in range(H):
            for j in range(W):
                if grid[i][j]==c and not seen[i][j]:
                    que = deque([(i,j)])
                    seen[i][j]=True
                    pts = []
                    while que:
                        x,y = que.popleft()
                        pts.append((x,y))
                        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx,ny = x+dx, y+dy
                            if 0<=nx<H and 0<=ny<W and not seen[nx][ny] and grid[nx][ny]==c:
                                seen[nx][ny]=True
                                que.append((nx,ny))
                    minr = min(x for x,y in pts)
                    maxr = max(x for x,y in pts)
                    minc = min(y for x,y in pts)
                    maxc = max(y for x,y in pts)
                    shape = [(x-minr, y-minc) for x,y in pts]
                    comps.append((minr, minc, maxr-minr+1, maxc-minc+1, shape, c))
        return comps
    all_comps = {c: find_comps(c) for c in colors}
    top = []; bot = []
    for c in colors:
        comps = sorted(all_comps[c], key=lambda x: (x[0], x[2]))
        top.append(comps[0])
        bot.append(comps[1])
    small_h = max(b[2] for b in bot)
    big_h = max(t[2] for t in top)
    spacer = 1
    small_r0 = H - (small_h + spacer + big_h)
    big_r0 = small_r0 + small_h + spacer
    out = [[0]*W for _ in range(H)]
    def place(comps, r0, region_h):
        widths = [c[3] for c in comps]
        total_w = sum(widths)
        gap = W - total_w
        inter = gap//(len(comps)+1)
        x = inter
        for minr, minc, h, w, shape, col in comps:
            y0 = r0 if h==region_h else r0 + region_h - h
            for dx,dy in shape:
                rr = y0 + dx
                cc = x + dy
                out[rr][cc] = col
            x += w + inter
    place(bot, small_r0, small_h)
    place(top, big_r0, big_h)
    return out