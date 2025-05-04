from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    regions = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==6 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==6:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                            comp.append((nx,ny))
                regions.append(comp)
    if regions:
        # pick largest region
        comp = max(regions, key=len)
        rows = [r for r,c in comp]
        cols = [c for r,c in comp]
        r0,r1 = min(rows), max(rows)
        c0,c1 = min(cols), max(cols)
        for r in range(r0,r1+1):
            for c in range(c0,c1+1):
                if (r,c) in comp:
                    out[r][c] = 7
        out[r0][c0] = 1
        out[r1][c1] = 9
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j]==5 and grid[i][j+1]==5 and grid[i+1][j]==5 and grid[i+1][j+1]==5:
                for di,dj in ((-2,0),(0,-2),(2,0),(0,2)):
                    ii, jj = i+di, j+dj
                    if 0<=ii<h-1 and 0<=jj<w-1:
                        block = [grid[ii][jj],grid[ii][jj+1],grid[ii+1][jj],grid[ii+1][jj+1]]
                        if all(v in (1,3) for v in block):
                            for a in (ii,ii+1):
                                for b in (jj,jj+1):
                                    out[a][b] = 3 if grid[a][b]==1 else 1
    return out