def solve(grid):
    h = len(grid)
    w = len(grid[0])
    visited = [[False]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 1 and not visited[r][c]:
                comp = []
                stack = [(r, c)]
                visited[r][c] = True
                while stack:
                    rr, cc = stack.pop()
                    comp.append((rr, cc))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == 1:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                if len(comp) > 1:
                    rs = [p[0] for p in comp]
                    cs = [p[1] for p in comp]
                    r0, r1 = min(rs), max(rs)
                    c0, c1 = min(cs), max(cs)
                    sr = r0 + r1
                    sc = c0 + c1
                    sym = True
                    comp_set = set(comp)
                    for rr, cc in comp:
                        if (sr-rr, cc) not in comp_set or (rr, sc-cc) not in comp_set:
                            sym = False
                            break
                    if sym:
                        for rr, cc in comp:
                            grid[rr][cc] = 2
    return grid