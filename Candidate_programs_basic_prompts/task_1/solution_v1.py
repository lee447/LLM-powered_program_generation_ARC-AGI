def solve(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    res = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0 and not visited[r][c]:
                stack = [(r,c)]
                visited[r][c] = True
                pts = []
                while stack:
                    pr, pc = stack.pop()
                    pts.append((pr,pc,grid[pr][pc]))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = pr+dr, pc+dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                if len(pts) >= 6:
                    rmin = min(p[0] for p in pts)
                    rmax = max(p[0] for p in pts)
                    cmin = min(p[1] for p in pts)
                    cmax = max(p[1] for p in pts)
                    col_colors = {}
                    for pr, pc, pv in pts:
                        col_colors.setdefault(pc, {})
                        col_colors[pc][pv] = col_colors[pc].get(pv,0) + 1
                    for cc in range(cmin, cmax+1):
                        if cc in col_colors:
                            chosen = max(col_colors[cc].items(), key=lambda x: x[1])[0]
                        else:
                            continue
                        for rr in range(rmin, rmax+1):
                            res[rr][cc] = chosen
    return res