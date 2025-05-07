from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not seen[i][j]:
                stk = [(i,j)]
                seen[i][j] = True
                comp = []
                while stk:
                    r,c = stk.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]==5:
                            seen[nr][nc] = True
                            stk.append((nr,nc))
                shapes.append(comp)
    for comp in shapes:
        rs = [r for r,c in comp]
        cs = [c for r,c in comp]
        minr, maxr = min(rs), max(rs)
        minc, maxc = min(cs), max(cs)
        hole_cols = [c for c in range(minc, maxc+1) if grid[minr][c] != 5]
        if not hole_cols: continue
        hole = hole_cols[0]
        center = (minc + maxc) / 2
        # fill interior and hole
        for r in range(minr, maxr+1):
            for c in range(minc, maxc+1):
                if grid[r][c] == 0:
                    out[r][c] = 2
        # draw baseline
        br = minr - 1
        if br >= 0:
            if hole < center:
                for c in range(hole, w):
                    if out[br][c] == 0:
                        out[br][c] = 2
            else:
                for c in range(0, hole+1):
                    if out[br][c] == 0:
                        out[br][c] = 2
    return out