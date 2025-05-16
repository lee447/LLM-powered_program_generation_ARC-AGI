from collections import deque
def solve(grid):
    H, W = len(grid), len(grid[0])
    bg = max({c:0 for row in grid for c in row}, key=lambda _:0)
    # determine true background
    cnt = {}
    for row in grid:
        for c in row:
            cnt[c] = cnt.get(c,0) + 1
    bg = max(cnt, key=cnt.get)
    vis = [[False]*W for _ in range(H)]
    blocks = []
    for y in range(H):
        for x in range(W):
            if grid[y][x] != bg and not vis[y][x]:
                q = deque([(y, x)])
                vis[y][x] = True
                comp = []
                while q:
                    yy, xx = q.popleft()
                    comp.append((yy, xx))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0 <= ny < H and 0 <= nx < W and not vis[ny][nx] and grid[ny][nx] != bg:
                            vis[ny][nx] = True
                            q.append((ny, nx))
                ys = [p[0] for p in comp]
                xs = [p[1] for p in comp]
                y0, y1 = min(ys), max(ys)
                x0, x1 = min(xs), max(xs)
                block = [row[x0:x1+1] for row in grid[y0:y1+1]]
                blocks.append((y0, x0, block))
    # no re-sorting: keep discovery order
    blocks = [b for _,_,b in blocks]
    H_out = max(len(b) for b in blocks)
    out = []
    for i in range(H_out):
        row = []
        for j, b in enumerate(blocks):
            h, w = len(b), len(b[0])
            top = (H_out - h)//2
            if i < top or i >= top + h:
                row += [bg]*w
            else:
                row += b[i - top]
            if j+1 < len(blocks):
                row += [bg]
        out.append(row)
    return out