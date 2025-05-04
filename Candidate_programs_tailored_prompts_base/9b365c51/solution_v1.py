def solve(grid):
    h, w = len(grid), len(grid[0])
    stripes = []
    for c in range(w):
        col_colors = [grid[r][c] for r in range(h) if grid[r][c] not in (0,8)]
        if col_colors and all(col_colors[0]==x for x in col_colors):
            stripes.append((c, col_colors[0]))
    stripes.sort(key=lambda x: x[0])
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for r in range(h):
        for c in range(w):
            if grid[r][c]==8 and not visited[r][c]:
                stack = [(r,c)]
                cells = []
                visited[r][c]=True
                while stack:
                    rr, cc = stack.pop()
                    cells.append((rr,cc))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==8:
                            visited[nr][nc]=True
                            stack.append((nr,nc))
                cx = sum(c for _,c in cells)/len(cells)
                clusters.append((cx, cells))
    clusters.sort(key=lambda x: x[0])
    out = [[0]*w for _ in range(h)]
    for ( _, (col, color) ), (__, cells) in zip(stripes, clusters):
        for r, c in cells:
            out[r][c] = color
    return out