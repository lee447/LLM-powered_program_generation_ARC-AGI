from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                c = grid[i][j]
                stack = [(i, j)]
                pts = []
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    pts.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == c:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                if len(pts) == 9:
                    rows = [x for x,_ in pts]
                    cols = [y for _,y in pts]
                    i0, i1 = min(rows), max(rows)
                    j0, j1 = min(cols), max(cols)
                    if i1 - i0 == 2 and j1 - j0 == 2:
                        for ii in range(i0, i1+1):
                            for jj in range(j0, j1+1):
                                out[ii][jj] = 0
                        out[i0][j0+1] = c
                        out[i0+1][j0] = c
                        out[i0+1][j1] = c
                        out[i1][j0+1] = c
    return out