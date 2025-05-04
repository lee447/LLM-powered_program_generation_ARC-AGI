from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==8 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==8:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                minr = min(r for r,_ in comp)
                maxr = max(r for r,_ in comp)
                minc = min(c for _,c in comp)
                maxc = max(c for _,c in comp)
                for rr in range(minr, maxr+1):
                    for cc in range(minc, maxc+1):
                        if res[rr][cc]==0:
                            res[rr][cc]=2
    return res