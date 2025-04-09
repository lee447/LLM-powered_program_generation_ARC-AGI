from collections import Counter
def solve(grid):
    n, m = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for j in range(m):
        out[0][j] = 0
        out[n-1][j] = 0
    for i in range(n):
        out[i][0] = 0
        out[i][m-1] = 0
    visited = [[False]*m for _ in range(n)]
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if not visited[i][j] and grid[i][j] != 0:
                stack = [(i,j)]
                comp = []
                while stack:
                    ci, cj = stack.pop()
                    if visited[ci][cj]:
                        continue
                    visited[ci][cj] = True
                    comp.append((ci,cj))
                    for di, dj in dirs:
                        ni, nj = ci+di, cj+dj
                        if 1 <= ni < n-1 and 1 <= nj < m-1:
                            if not visited[ni][nj] and grid[ni][nj] != 0:
                                stack.append((ni,nj))
                if len(comp) == 1:
                    for (ci, cj) in comp:
                        out[ci][cj] = 0
                else:
                    vals = [grid[ci][cj] for (ci,cj) in comp]
                    mode = Counter(vals).most_common(1)[0][0]
                    for (ci, cj) in comp:
                        out[ci][cj] = mode
    return out