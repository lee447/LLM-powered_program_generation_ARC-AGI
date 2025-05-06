from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    res = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == 8:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                rs = [r for r,_ in comp]
                cs = [c for _,c in comp]
                r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
                for r in range(r0, r1+1):
                    for c in range(c0, c1+1):
                        if res[r][c] == 0:
                            res[r][c] = 2
    return res