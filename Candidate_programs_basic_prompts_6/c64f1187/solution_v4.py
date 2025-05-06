from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    five_coords = [(r,c) for r in range(R) for c in range(C) if grid[r][c]==5]
    if not five_coords:
        return []
    minr5 = min(r for r,_ in five_coords)
    maxr5 = max(r for r,_ in five_coords)
    minc5 = min(c for _,c in five_coords)
    maxc5 = max(c for _,c in five_coords)
    # find clusters of 1's in top region (r < minr5)
    seen = [[False]*C for _ in range(R)]
    clusters = []
    for r in range(minr5):
        for c in range(C):
            if grid[r][c]==1 and not seen[r][c]:
                q=[(r,c)]
                seen[r][c]=True
                comp=[]
                for x,y in q:
                    comp.append((x,y))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = x+dr, y+dc
                        if 0<=nr<R and 0<=nc<C and nr<minr5 and grid[nr][nc]==1 and not seen[nr][nc]:
                            seen[nr][nc]=True
                            q.append((nr,nc))
                clusters.append(comp)
    # derive footprints
    footprints = {}
    for comp in clusters:
        r_min = min(r for r,_ in comp)
        c_min = min(c for _,c in comp)
        dt_r, dt_c = r_min-1, c_min-1
        if not (0<=dt_r<R and 0<=dt_c<C):
            continue
        color = grid[dt_r][dt_c]
        if color==0 or color==1 or color==5:
            continue
        offs = [(r-dt_r, c-dt_c) for r,c in comp]
        footprints[color] = offs
    # find bottom dots
    dots = []
    for r in range(minr5, maxr5+1):
        for c in range(minc5, maxc5+1):
            v = grid[r][c]
            if v in footprints:
                dots.append((r,c,v))
    # collect placements
    pts = []
    for r,c,v in dots:
        for dr,dc in footprints[v]:
            pts.append((r+dr, c+dc, v))
    if not pts:
        return []
    minr = min(r for r,_,_ in pts)
    maxr = max(r for r,_,_ in pts)
    minc = min(c for _,c,_ in pts)
    maxc = max(c for _,c,_ in pts)
    out = [[0]*(maxc-minc+1) for _ in range(maxr-minr+1)]
    for r,c,v in pts:
        out[r-minr][c-minc] = v
    return out