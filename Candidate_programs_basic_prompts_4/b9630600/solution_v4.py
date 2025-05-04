from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==3 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==3:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                rs = [r for r,_ in comp]
                cs = [c for _,c in comp]
                minr, maxr = min(rs), max(rs)
                minc, maxc = min(cs), max(cs)
                if maxr-minr>=2 and maxc-minc>=2:
                    for c in range(minc+1, maxc):
                        res[minr+1][c] = 3
                        res[maxr-1][c] = 3
                    for r in range(minr+1, maxr):
                        res[r][minc+1] = 3
                        res[r][maxc-1] = 3
    return res