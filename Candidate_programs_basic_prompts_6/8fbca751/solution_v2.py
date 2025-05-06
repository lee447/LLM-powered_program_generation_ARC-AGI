def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                min_r, max_r = i, i
                min_c, max_c = j, j
                while stack:
                    r, c = stack.pop()
                    comp.append((r,c))
                    if r<min_r: min_r=r
                    if r>max_r: max_r=r
                    if c<min_c: min_c=c
                    if c>max_c: max_c=c
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==8:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                for r in range(min_r, max_r+1):
                    for c in range(min_c, max_c+1):
                        if res[r][c] != 8:
                            res[r][c] = 2
    return res