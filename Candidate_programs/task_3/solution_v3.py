from collections import deque
from copy import deepcopy
def solve(grid):
    R, C = len(grid), len(grid[0])
    out = deepcopy(grid)
    vis = [[False]*C for _ in range(R)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    comps = []
    for i in range(R):
        for j in range(C):
            if grid[i][j]==1 and not vis[i][j]:
                comp = []
                q = deque([(i,j)])
                vis[i][j] = True
                while q:
                    r,c = q.popleft()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<R and 0<=nc<C and grid[nr][nc]==1 and not vis[nr][nc]:
                            vis[nr][nc] = True
                            q.append((nr,nc))
                comps.append(comp)
    for comp in comps:
        rs = [r for r,c in comp]
        cs = [c for r,c in comp]
        top, bot, left, right = min(rs), max(rs), min(cs), max(cs)
        h = bot - top + 1
        if h>=8:
            stroke_top = 2
            stroke_bot = 3
        else:
            stroke_top = 4
            stroke_bot = 3
        rowsInComp = {}
        for r,c in comp:
            rowsInComp.setdefault(r, []).append(c)
        for r in sorted(rowsInComp):
            if r==top or r==bot:
                continue
            cols = sorted(rowsInComp[r])
            run = []
            for c in cols:
                if run and c==run[-1]+1:
                    run.append(c)
                else:
                    if len(run)>=3:
                        rel = (r-top)/(h-1) if h>1 else 0
                        sc = stroke_top if rel < 0.5 else stroke_bot
                        for cc in run[1:-1]:
                            out[r][cc] = sc
                    run = [c]
            if len(run)>=3:
                rel = (r-top)/(h-1) if h>1 else 0
                sc = stroke_top if rel < 0.5 else stroke_bot
                for cc in run[1:-1]:
                    out[r][cc] = sc
    return out