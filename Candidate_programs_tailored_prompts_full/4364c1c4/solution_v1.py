def solve(grid):
    h, w = len(grid), len(grid[0])
    flat = [c for row in grid for c in row]
    bg = max(set(flat), key=flat.count)
    g = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if not vis[i][j] and g[i][j] != bg:
                col = g[i][j]
                pts = []
                stack = [(i,j)]
                vis[i][j] = True
                while stack:
                    r,c = stack.pop()
                    pts.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not vis[nr][nc] and g[nr][nc]==col:
                            vis[nr][nc] = True
                            stack.append((nr,nc))
                rs = [r for r,c in pts]
                cs = [c for r,c in pts]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                holes = [c for c in range(c0, c1+1) if g[r0+(r1-r0)//2][c]==bg and r0<r1]
                if not holes:
                    holes = [c for c in range(c0, c1+1) if g[r1-1][c]==bg]
                    rr = r1-1
                else:
                    rr = r0+(r1-r0)//2
                for c in holes:
                    m = c0 + c1 - c
                    g[rr][c] = col
                    g[rr][m] = bg
                # shift
                left = min(c for r,c in pts if g[r][c]==col)
                shift = -left+1
                new = [[g[r][c] for c in range(w)] for r in range(h)]
                for r,c in pts:
                    if g[r][c]==col:
                        new[r][c] = bg
                        new[r][c+shift] = col
                g = new
    return g