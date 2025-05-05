def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                color = grid[i][j]
                stack = [(i, j)]
                comp = []
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == color:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                mr = min(r for r,c in comp)
                mc = min(c for r,c in comp)
                clusters.append((mr, mc, comp, color))
    clusters.sort(key=lambda x:(x[0], x[1]))
    _, _, comp, color = clusters[0]
    minr = min(r for r,c in comp)
    maxr = max(r for r,c in comp)
    minc = min(c for r,c in comp)
    maxc = max(c for r,c in comp)
    out_h = maxr - minr + 1
    out_w = maxc - minc + 1
    out = [[0]*out_w for _ in range(out_h)]
    for r, c in comp:
        out[r-minr][c-minc] = color
    return out