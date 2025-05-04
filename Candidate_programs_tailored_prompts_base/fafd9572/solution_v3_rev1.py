from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                mr = min(r for r,c in comp)
                mc = min(c for r,c in comp)
                comps.append((mr,mc,comp))
    anchors = sorted((i,j,grid[i][j]) for i in range(h) for j in range(w) if grid[i][j] > 1)
    palette = sorted({v for _,_,v in anchors})
    out = [row[:] for row in grid]
    if len(palette) == 2:
        row_has = [any(grid[r][c] == 1 for c in range(w)) for r in range(h)]
        rows = []
        r = 0
        while r < h:
            if row_has[r]:
                s = r
                while r+1 < h and row_has[r+1]:
                    r += 1
                rows.append((s, r))
            r += 1
        col_has = [any(grid[r][c] == 1 for r in range(h)) for c in range(w)]
        cols = []
        c = 0
        while c < w:
            if col_has[c]:
                s = c
                while c+1 < w and col_has[c+1]:
                    c += 1
                cols.append((s, c))
            c += 1
        for mr, mc, comp in comps:
            ri = next(i for i,(a,b) in enumerate(rows) if a <= mr <= b)
            ci = next(j for j,(a,b) in enumerate(cols) if a <= mc <= b)
            color = palette[(ri + ci) % 2]
            for r,c in comp:
                out[r][c] = color
    else:
        comps.sort(key=lambda x:(x[0],x[1]))
        vals = [v for _,_,v in anchors]
        for (mr,mc,comp), color in zip(comps, vals):
            for r,c in comp:
                out[r][c] = color
    return out