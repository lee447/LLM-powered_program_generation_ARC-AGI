from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    out = [row[:] for row in grid]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    comp.append((r,c))
                    for dr, dc in dirs:
                        rr, cc = r+dr, c+dc
                        if 0 <= rr < m and 0 <= cc < n and not visited[rr][cc] and grid[rr][cc] != 0:
                            visited[rr][cc] = True
                            stack.append((rr,cc))
                rs = [r for r,_ in comp]
                cs = [c for _,c in comp]
                minr, maxr = min(rs), max(rs)
                minc, maxc = min(cs), max(cs)
                seed_rows = [r for r in range(minr, maxr+1) if len({grid[r][c] for c in range(minc, maxc+1) if grid[r][c]!=0})>1]
                if seed_rows:
                    D = {r:{c:grid[r][c] for c in range(minc, maxc+1) if grid[r][c]!=0} for r in seed_rows}
                    k = len(seed_rows)
                    for r in range(minr, maxr+1):
                        idx = (r-minr) % k
                        src = seed_rows[idx]
                        for c, v in D[src].items():
                            out[r][c] = v
                else:
                    seed_cols = [c for c in range(minc, maxc+1) if len({grid[r][c] for r in range(minr, maxr+1) if grid[r][c]!=0})>1]
                    if seed_cols:
                        D2 = {c:{r:grid[r][c] for r in range(minr, maxr+1) if grid[r][c]!=0} for c in seed_cols}
                        k2 = len(seed_cols)
                        for c in range(minc, maxc+1):
                            idx = (c-minc) % k2
                            src = seed_cols[idx]
                            for r, v in D2[src].items():
                                out[r][c] = v
    return out