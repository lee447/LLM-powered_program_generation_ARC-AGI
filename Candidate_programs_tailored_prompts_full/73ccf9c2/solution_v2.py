from typing import List, Tuple

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
                minr, minc, maxr, maxc = i, j, i, j
                while stack:
                    r, c = stack.pop()
                    coords.append((r,c))
                    if r < minr: minr = r
                    if r > maxr: maxr = r
                    if c < minc: minc = c
                    if c > maxc: maxc = c
                    for dr in (-1,0,1):
                        for dc in (-1,0,1):
                            if dr==0 and dc==0: continue
                            nr, nc = r+dr, c+dc
                            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc]==color:
                                visited[nr][nc] = True
                                stack.append((nr,nc))
                clusters.append((minr, minc, maxr, maxc, color, coords))
    clusters.sort(key=lambda x: (x[0], x[1]))
    minr, minc, maxr, maxc, color, coords = clusters[0]
    rh, rw = maxr-minr+1, maxc-minc+1
    out = [[0]*rw for _ in range(rh)]
    for r, c in coords:
        out[r-minr][c-minc] = color
    return out