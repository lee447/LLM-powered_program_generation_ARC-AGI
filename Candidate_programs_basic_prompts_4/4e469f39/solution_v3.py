from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not seen[i][j]:
                stack = [(i,j)]
                comp = []
                seen[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]==5:
                            seen[nr][nc]=True
                            stack.append((nr,nc))
                rs = [r for r,c in comp]
                cs = [c for r,c in comp]
                minr, maxr = min(rs), max(rs)
                minc, maxc = min(cs), max(cs)
                hole = None
                for c in range(minc, maxc+1):
                    if grid[minr][c]!=5:
                        hole = (minr, c)
                        break
                if hole is None:
                    for c in range(minc, maxc+1):
                        if grid[maxr][c]!=5:
                            hole = (maxr, c)
                            break
                if hole is None:
                    for r in range(minr, maxr+1):
                        if grid[r][minc]!=5:
                            hole = (r, minc)
                            break
                if hole is None:
                    for r in range(minr, maxr+1):
                        if grid[r][maxc]!=5:
                            hole = (r, maxc)
                            break
                hr, hc = hole
                if hr==minr:
                    ar, ac = hr-1, hc
                    center = (minc+maxc)/2
                    step = 1 if hc<center else -1
                    r0 = ar; c0 = ac
                    while 0<=c0<w and 0<=r0<h and res[r0][c0]==0:
                        res[r0][c0]=2
                        c0 += step
                elif hr==maxr:
                    ar, ac = hr+1, hc
                    center = (minc+maxc)/2
                    step = 1 if hc<center else -1
                    r0 = ar; c0 = ac
                    while 0<=c0<w and 0<=r0<h and res[r0][c0]==0:
                        res[r0][c0]=2
                        c0 += step
                elif hc==minc:
                    ar, ac = hr, hc-1
                    center = (minr+maxr)/2
                    step = 1 if hr<center else -1
                    r0 = ar; c0 = ac
                    while 0<=c0<w and 0<=r0<h and res[r0][c0]==0:
                        res[r0][c0]=2
                        r0 += step
                else:
                    ar, ac = hr, hc+1
                    center = (minr+maxr)/2
                    step = 1 if hr<center else -1
                    r0 = ar; c0 = ac
                    while 0<=c0<w and 0<=r0<h and res[r0][c0]==0:
                        res[r0][c0]=2
                        r0 += step
                for rr in range(minr+1, maxr):
                    for cc in range(minc+1, maxc):
                        if res[rr][cc]==0:
                            res[rr][cc]=2
    return res