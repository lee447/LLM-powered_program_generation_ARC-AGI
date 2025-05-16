from typing import List
from collections import deque, Counter, defaultdict

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cnt = Counter(c for row in grid for c in row)
    bg = max(cnt, key=cnt.get)
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if not vis[i][j] and grid[i][j] != bg:
                col = grid[i][j]
                pts = []
                dq = deque([(i, j)])
                vis[i][j] = True
                while dq:
                    y, x = dq.popleft()
                    pts.append((y, x))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < h and 0 <= nx < w and not vis[ny][nx] and grid[ny][nx] == col:
                            vis[ny][nx] = True
                            dq.append((ny, nx))
                ys = [y for y,_ in pts]
                xs = [x for _,x in pts]
                comps.append((col, pts, min(ys), min(xs), max(ys)-min(ys)+1, max(xs)-min(xs)+1))
    one = [c for c in comps if len(c[1]) == 1]
    blocks = [c for c in comps if len(c[1]) > 1]
    blocks.sort(key=lambda c: c[3])
    colcnt = Counter(c[3] for c in one)
    drive_cols = [c for c,_ in colcnt.most_common(len(blocks))]
    drive_cols.sort()
    one_by_col = defaultdict(list)
    color_by_pt = {}
    for col, pts, _, x, _, _ in one:
        y = pts[0][0]
        one_by_col[x].append(y)
        color_by_pt[(y, x)] = grid[y][x]
    out = [row[:] for row in grid]
    for bidx, (_, pts, minr, minc, bh, _) in enumerate(blocks):
        dc = drive_cols[bidx]
        drs = sorted(one_by_col[dc])
        spacing = drs[1] - drs[0]
        period = bh + spacing
        sign = 1 if minr < drs[-1] else -1
        for k in range(1, len(drs)):
            newr = minr + sign * period * k
            if not (0 <= newr <= h - bh):
                continue
            color = color_by_pt[(drs[k], dc)]
            for y, x in pts:
                out[newr + (y - minr)][x] = color
    return out