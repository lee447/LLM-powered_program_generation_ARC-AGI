from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] in (2,5) and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                pts = []
                while stack:
                    r,c = stack.pop()
                    pts.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc] in (2,5):
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                clusters.append(pts)
    cl1, cl2 = clusters
    if sum(r for r,_ in cl1)/len(cl1) > sum(r for r,_ in cl2)/len(cl2):
        top, bottom = cl2, cl1
    else:
        top, bottom = cl1, cl2
    if sum(c for _,c in top)/len(top) > sum(c for _,c in bottom)/len(bottom):
        left, right = bottom, top
    else:
        left, right = top, bottom
    tmaxr = max(r for r,_ in top)
    bminr = min(r for r,_ in bottom)
    lmaxc = max(c for _,c in left)
    rminc = min(c for _,c in right)
    out = [[grid[r][c] if grid[r][c] != 4 else 0 for c in range(w)] for r in range(h)]
    for r in range(tmaxr+1, bminr):
        for c in range(lmaxc+1, rminc):
            if out[r][c] == 0:
                out[r][c] = 4
    for r in range(tmaxr, bminr+1):
        if out[r][lmaxc] == 0:
            out[r][lmaxc] = 4
    for c in range(lmaxc, rminc+1):
        if out[bminr][c] == 0:
            out[bminr][c] = 4
    return out