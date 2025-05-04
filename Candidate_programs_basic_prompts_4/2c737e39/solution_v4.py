from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                col = grid[i][j]
                comp = []
                stack = [(i,j)]
                visited[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] != 0:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                comps.append(comp)
    pattern = max(comps, key=len)
    marker = next(c for c in comps if len(c)==1 and grid[c[0][0]][c[0][1]]==5)
    pr = next((r,c) for r,c in pattern if grid[r][c]==5)
    mr, mc = marker[0]
    dr, dc = mr-pr[0], mc-pr[1]
    out = [row[:] for row in grid]
    for r,c in pattern:
        v = grid[r][c]
        if v != 5:
            nr, nc = r+dr, c+dc
            out[nr][nc] = v
    return out