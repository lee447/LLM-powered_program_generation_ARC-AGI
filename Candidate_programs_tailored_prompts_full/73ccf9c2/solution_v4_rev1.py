from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                color = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                coords = []
                minr = maxr = i
                minc = maxc = j
                while stack:
                    r, c = stack.pop()
                    coords.append((r,c))
                    if r<minr: minr=r
                    if r>maxr: maxr=r
                    if c<minc: minc=c
                    if c>maxc: maxc=c
                    for dr in (-1,0,1):
                        for dc in (-1,0,1):
                            if dr==0 and dc==0: continue
                            nr, nc = r+dr, c+dc
                            if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==color:
                                visited[nr][nc] = True
                                stack.append((nr,nc))
                clusters.append((minr, minc, maxr, maxc, color, coords))
    midr = h/2.0
    midc = w/2.0
    candidates = [c for c in clusters if c[0]>midr and c[1]<midc]
    if not candidates:
        return []
    minr, minc, maxr, maxc, color, coords = sorted(candidates, key=lambda x:(x[0],x[1]))[0]
    rh = maxr-minr+1
    rw = maxc-minc+1
    out = [[0]*rw for _ in range(rh)]
    for r, c in coords:
        out[r-minr][c-minc] = color
    return out