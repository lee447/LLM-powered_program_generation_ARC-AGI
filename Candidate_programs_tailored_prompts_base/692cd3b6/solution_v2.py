from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                colset, stack = [], [(i,j)]
                seen[i][j] = True
                while stack:
                    r,c = stack.pop()
                    colset.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc] in (2,5):
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                clusters.append(colset)
    cs = sorted(clusters, key=lambda cl: sum(r for r,_ in cl)/len(cl))
    top, bottom = cs[0], cs[1]
    tminr = min(r for r,_ in top)
    tmaxr = max(r for r,_ in top)
    tminc = min(c for _,c in top)
    tmaxc = max(c for _,c in top)
    bminr = min(r for r,_ in bottom)
    bmaxr = max(r for r,_ in bottom)
    bminc = min(c for _,c in bottom)
    bmaxc = max(c for _,c in bottom)
    if tminc < bminc:
        lc, rc = top, bottom
        lminc, lmaxc = tminc, tmaxc
        rminc, rmaxc = bminc, bmaxc
    else:
        lc, rc = bottom, top
        lminc, lmaxc = bminc, bmaxc
        rminc, rmaxc = tminc, tmaxc
    if tminr < bminr:
        uc, dc = top, bottom
        uminr, umaxr = tminr, tmaxr
        dminr, dmaxr = bminr, bmaxr
    else:
        uc, dc = bottom, top
        uminr, umaxr = bminr, bmaxr
        dminr, dmaxr = tminr, tmaxr
    out = [row[:] for row in grid]
    for r in range(umaxr, dminr+1):
        for c in range(lmaxc, rminc+1):
            if out[r][c] == 0:
                out[r][c] = 4
    return out