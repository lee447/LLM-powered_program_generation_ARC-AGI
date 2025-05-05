def solve(grid):
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                seen[i][j] = True
                cells = []
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not seen[nr][nc] and grid[nr][nc] == col:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                comps.append(cells)
    best = None
    best_score = None
    for cells in comps:
        s = sum(r+c for r,c in cells)/len(cells)
        if best_score is None or s < best_score:
            best_score = s
            best = cells
    rs = [r for r,c in best]
    cs = [c for r,c in best]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    out_h = r1 - r0 + 1
    out_w = c1 - c0 + 1
    col = grid[best[0][0]][best[0][1]]
    out = [[0]*out_w for _ in range(out_h)]
    for r,c in best:
        out[r-r0][c-c0] = col
    return out