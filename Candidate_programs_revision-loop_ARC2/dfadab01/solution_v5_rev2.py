from typing import List
from collections import Counter

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not vis[i][j]:
                c = grid[i][j]
                stack = [(i, j)]
                vis[i][j] = True
                minr, minc, maxr, maxc = i, j, i, j
                cnt = 0
                while stack:
                    r, cc = stack.pop()
                    cnt += 1
                    minr, minc = min(minr, r), min(minc, cc)
                    maxr, maxc = max(maxr, r), max(maxc, cc)
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, cc+dc
                        if 0<=nr<h and 0<=nc<w and not vis[nr][nc] and grid[nr][nc]==c:
                            vis[nr][nc] = True
                            stack.append((nr, nc))
                comps.append((minr, minc, maxr, maxc, c, cnt))
    reps = [(r, c, col) for r, c, R, C, col, cnt in comps]
    counts = Counter(col for _,_,col in reps)
    m = [(r,c,col) for r,c,col in reps if col in (1,2,3,5,8)]
    rs = sorted({r for r,_,_ in m})
    cs = sorted({c_ for _,c_,_ in m})
    drs = [rs[i+1]-rs[i] for i in range(len(rs)-1)]
    dcs = [cs[i+1]-cs[i] for i in range(len(cs)-1)]
    d = [d for d in drs+dcs if d>1]
    if d:
        step = Counter(d).most_common(1)[0][0]
    else:
        step = max(h, w)
    H = step-1 if step>4 else step
    rmod = [r % step for r,_,_ in m]
    cmod = [c_ % step for _,c_,_ in m]
    shiftR = Counter(rmod).most_common(1)[0][0]
    shiftC = Counter(cmod).most_common(1)[0][0]
    out = [[0]*w for _ in range(h)]
    for r, c, col in m:
        if (r-shiftR) % step or (c-shiftC) % step:
            continue
        if col == 2 or col == 3:
            p_type = 'ring'
            out_col = 4 if col==2 else 1
        elif col == 1 or col == 5:
            p_type = 'quarter'
            out_col = 1 if col==1 else 6
        elif col == 8:
            p_type = 'x'
            out_col = 7
        else:
            continue
        for i in range(H):
            for j in range(H):
                if p_type == 'ring':
                    val = (i==0 or i==H-1 or j==0 or j==H-1)
                elif p_type == 'quarter':
                    val = (i<H//2 and j<H//2) or (i>=H//2 and j>=H//2)
                else:
                    val = (i==j or i+j==H-1)
                if val and 0<=r+i<h and 0<=c+j<w:
                    out[r+i][c+j] = out_col
    return out