def solve(grid):
    h = len(grid)
    w = len(grid[0])
    visited = [[False]*w for _ in range(h)]
    clusters = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not visited[i][j]:
                stack = [(i,j)]
                comp = []
                minr = i
                visited[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    if r<minr: minr = r
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==1:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                clusters.append((minr,comp))
    if not clusters:
        return [row[:] for row in grid]
    keep = max(clusters, key=lambda x:x[0])[1]
    target = grid[0][0]
    res = [row[:] for row in grid]
    for minr,comp in clusters:
        if comp is not keep:
            for r,c in comp:
                res[r][c] = target
    return res