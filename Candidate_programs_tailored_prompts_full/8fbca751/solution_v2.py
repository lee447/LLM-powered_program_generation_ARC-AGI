from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==8 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j]=True
                minr, maxr, minc, maxc = i, i, j, j
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    if r<minr: minr=r
                    if r>maxr: maxr=r
                    if c<minc: minc=c
                    if c>maxc: maxc=c
                    for dr,dc in dirs:
                        rr,cc = r+dr, c+dc
                        if 0<=rr<h and 0<=cc<w and not visited[rr][cc] and grid[rr][cc]==8:
                            visited[rr][cc]=True
                            stack.append((rr,cc))
                for r in range(minr, maxr+1):
                    for c in range(minc, maxc+1):
                        if grid[r][c]==0:
                            grid[r][c]=2
    return grid