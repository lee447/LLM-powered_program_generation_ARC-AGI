import numpy as np

def solve(grid):
    g = np.array(grid)
    h, w = g.shape
    vis = np.zeros((h, w), bool)
    comps = []
    for i in range(h):
        for j in range(w):
            if not vis[i, j]:
                col = g[i, j]
                stack = [(i, j)]
                pts = []
                vis[i, j] = True
                while stack:
                    x, y = stack.pop()
                    pts.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not vis[nx, ny] and g[nx, ny] == col:
                            vis[nx, ny] = True
                            stack.append((nx, ny))
                rs = [p[0] for p in pts]
                cs = [p[1] for p in pts]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                area = (r1 - r0 + 1) * (c1 - c0 + 1)
                if len(pts) == area and area > 1 and (r1-r0)==(c1-c0):
                    comps.append((r0, r1, c0, c1))
    r0, r1, c0, c1 = max(comps, key=lambda x: (x[1]-x[0]+1))
    n = r1 - r0 + 1
    # try four directions for a full n×n candidate
    if r0 >= n:
        cand = g[r0-n:r0, c0:c1+1]
        d = 'up'
    elif h - 1 - r1 >= n:
        cand = g[r1+1:r1+1+n, c0:c1+1]
        d = 'down'
    elif c0 >= n:
        cand = g[r0:r1+1, c0-n:c0]
        d = 'left'
    else:
        cand = g[r0:r1+1, c1+1:c1+1+n]
        d = 'right'
    # shrink off one layer on the side touching the block
    if d in ('up', 'down'):
        cand = cand[1:-1, :]
    else:
        cand = cand[:, 1:-1]
    return cand.tolist()