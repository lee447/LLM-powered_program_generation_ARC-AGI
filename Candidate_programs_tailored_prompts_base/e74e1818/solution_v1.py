def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    res = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                color = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == color:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                minr = min(r for r,c in comp)
                maxr = max(r for r,c in comp)
                minc = min(c for r,c in comp)
                maxc = max(c for r,c in comp)
                sub = [grid[r][minc:maxc+1] for r in range(minr, maxr+1)]
                rev = sub[::-1]
                for dr, row in enumerate(rev):
                    for dc, val in enumerate(row):
                        res[minr+dr][minc+dc] = val
    return res