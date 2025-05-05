import numpy as np
def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    centers = []
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=0 and not visited[r][c]:
                v=grid[r][c]
                if c+2<w and grid[r][c+1]==v and grid[r][c+2]==v:
                    visited[r][c]=visited[r][c+1]=visited[r][c+2]=True
                    centers.append((r,c+1))
                elif r+2<h and grid[r+1][c]==v and grid[r+2][c]==v:
                    visited[r][c]=visited[r+1][c]=visited[r+2][c]=True
                    centers.append((r+1,c))
    out = [row[:] for row in grid]
    byrow = {}
    for r,c in centers:
        byrow.setdefault(r,[]).append(c)
    for r, cols in byrow.items():
        cols.sort()
        for i in range(len(cols)-1):
            c1, c2 = cols[i], cols[i+1]
            for x in range(min(c1,c2)+1, max(c1,c2)):
                if out[r][x]==0: out[r][x]=2
    bycol = {}
    for r,c in centers:
        bycol.setdefault(c,[]).append(r)
    for c, rows in bycol.items():
        rows.sort()
        for i in range(len(rows)-1):
            r1, r2 = rows[i], rows[i+1]
            for y in range(min(r1,r2)+1, max(r1,r2)):
                if out[y][c]==0: out[y][c]=2
    return out