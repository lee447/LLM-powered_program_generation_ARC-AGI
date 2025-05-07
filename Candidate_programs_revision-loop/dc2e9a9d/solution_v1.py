from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 3 and not visited[i][j]:
                stack = [(i,j)]
                coords = []
                visited[i][j] = True
                while stack:
                    r,c = stack.pop()
                    coords.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 3 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                rs = [r for r,c in coords]
                cs = [c for r,c in coords]
                shapes.append((min(rs), max(rs), min(cs), max(cs), coords))
    best_r = None
    best_r_shape = None
    for shape in shapes:
        minr, maxr, minc, maxc, coords = shape
        sh = maxr-minr+1
        sw = maxc-minc+1
        if minr == 0: continue
        right_space = w - (maxc+1)
        if right_space >= sw:
            ok = True
            for r in range(minr, maxr+1):
                for c in range(maxc+1, maxc+1+sw):
                    if grid[r][c] != 0:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                if best_r is None or minr < best_r:
                    best_r = minr
                    best_r_shape = shape
    best_u = None
    best_u_shape = None
    for shape in shapes:
        minr, maxr, minc, maxc, coords = shape
        sh = maxr-minr+1
        sw = maxc-minc+1
        if minr >= sh:
            ok = True
            for r in range(minr-sh, minr):
                for c in range(minc, maxc+1):
                    if grid[r][c] != 0:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                if best_u is None or maxr > best_u:
                    best_u = maxr
                    best_u_shape = shape
    res = [row[:] for row in grid]
    if best_r_shape:
        minr, maxr, minc, maxc, coords = best_r_shape
        for r,c in coords:
            rr = r
            cc = maxc+1 + (c-minc)
            res[rr][cc] = 1
    if best_u_shape:
        minr, maxr, minc, maxc, coords = best_u_shape
        sh = maxr-minr+1
        for r,c in coords:
            rr = minr-sh + (r-minr)
            cc = c
            res[rr][cc] = 8
    return res