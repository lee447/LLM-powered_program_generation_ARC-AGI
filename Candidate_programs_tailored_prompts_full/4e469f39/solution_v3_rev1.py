from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    used = [[False]*w for _ in range(h)]
    out = [row[:] for row in grid]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not used[i][j]:
                stack=[(i,j)]
                used[i][j]=True
                cells=[]
                while stack:
                    r,c=stack.pop()
                    cells.append((r,c))
                    for dr,dc in dirs:
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and not used[nr][nc] and grid[nr][nc]==5:
                            used[nr][nc]=True
                            stack.append((nr,nc))
                rs=[r for r,_ in cells]; cs=[c for _,c in cells]
                r0,r1=min(rs),max(rs); c0,c1=min(cs),max(cs)
                for c in range(c0,c1+1):
                    if grid[r0][c]==0:
                        out[r0][c]=2
                for r in range(r0+1,r1):
                    for c in range(c0+1,c1):
                        if grid[r][c]==0:
                            out[r][c]=2
    return out