from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h,w = len(grid), len(grid[0])
    shape_rows = [i for i in range(h) if any(grid[i][j]==1 for j in range(w))]
    min_r, max_r = min(shape_rows), max(shape_rows)
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in shape_rows:
        for j in range(w):
            if grid[i][j]==1 and not seen[i][j]:
                pts = []
                dq = deque([(i,j)])
                seen[i][j] = True
                while dq:
                    x,y = dq.popleft()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==1 and min_r<=nx<=max_r:
                            seen[nx][ny] = True
                            dq.append((nx,ny))
                min_i = min(p[0] for p in pts)
                max_i = max(p[0] for p in pts)
                min_j = min(p[1] for p in pts)
                max_j = max(p[1] for p in pts)
                ph = max_i - min_i + 1
                pw = max_j - min_j + 1
                pat = [[1 if grid[min_i+di][min_j+dj]==1 else 0 for dj in range(pw)] for di in range(ph)]
                comps.append((min_j, pat))
    comps.sort(key=lambda x: x[0])
    id_list = [(c, grid[0][c]) for c in range(w) if grid[0][c]!=0]
    id_list.sort(key=lambda x: x[0])
    patterns = {}
    for k, (_, vid) in enumerate(id_list):
        if k < len(comps):
            patterns[vid] = comps[k][1]
    row_has = [any(grid[i][j]==5 and grid[i][j+1]==5 for j in range(w-1)) for i in range(h)]
    bands = [i for i in range(1,h-1) if row_has[i] and not row_has[i-1]]
    r0 = bands[0]
    jpos = [j for j in range(w-1) if grid[r0][j]==5 and grid[r0][j+1]==5]
    nb = len(jpos)
    vals = []
    for r in bands:
        row_vals = []
        for j in jpos:
            v = None
            for dr in (0,1):
                for dc in (0,1):
                    cv = grid[r+dr][j+dc]
                    if cv!=5:
                        v = cv
            row_vals.append(v)
        vals.append(row_vals)
    out_h = len(bands)*3 - 1
    out_w = nb*3 - 1
    out = [[0]*out_w for _ in range(out_h)]
    for bi in range(len(bands)):
        ro = bi*3
        for k in range(nb):
            vid = vals[bi][k]
            if vid is None or vid not in patterns:
                continue
            pat = patterns[vid]
            ph = len(pat)
            pw = len(pat[0])
            co = k*3
            for di in range(ph):
                for dj in range(pw):
                    if pat[di][dj]:
                        out[ro+di][co+dj] = vid
    return out