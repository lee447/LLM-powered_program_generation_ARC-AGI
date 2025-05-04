from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not vis[i][j]:
                stack = [(i,j)]
                comp = []
                vis[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not vis[nr][nc] and grid[nr][nc]==1:
                            vis[nr][nc] = True
                            stack.append((nr,nc))
                comps.append(comp)
    out = [row[:] for row in grid]
    for comp in comps:
        rs = [r for r,c in comp]
        cs = [c for r,c in comp]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        hh, ww = r1-r0+1, c1-c0+1
        size = len(comp)
        if hh==1 or ww==1:
            if size==hh*ww:
                for r,c in comp:
                    out[r][c] = 2
        else:
            border = 2*(hh+ww)-4
            if size==border and all(r==r0 or r==r1 or c==c0 or c==c1 for r,c in comp):
                for r,c in comp:
                    out[r][c] = 2
    return out