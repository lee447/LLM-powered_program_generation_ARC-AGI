def solve(grid):
    h, w = len(grid), len(grid[0])
    orig = grid
    new = [row[:] for row in orig]
    row_all4 = {r for r in range(h) if all(orig[r][c] == 4 for c in range(w))}
    col_all4 = {c for c in range(w) if all(orig[r][c] == 4 for r in range(h))}
    visited = [[False]*w for _ in range(h)]
    regions = []
    for i in range(h):
        for j in range(w):
            if orig[i][j] == 1 and not visited[i][j]:
                q = [(i,j)]
                visited[i][j] = True
                reg = []
                for r,c in q:
                    reg.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and orig[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                regions.append(reg)
    colors = {1:6, 2:8, 3:2}
    for reg in regions:
        rs = [r for r,_ in reg]; cs = [c for _,c in reg]
        minr, maxr = min(rs), max(rs)
        minc, maxc = min(cs), max(cs)
        for d, col in colors.items():
            for r in range(minr-d, maxr+d+1):
                for c in (minc-d, maxc+d):
                    if 0 <= r < h and 0 <= c < w and r not in row_all4 and c not in col_all4:
                        if orig[r][c] != 1:
                            new[r][c] = col
            for r in (minr-d, maxr+d):
                for c in range(minc-d, maxc+d+1):
                    if 0 <= r < h and 0 <= c < w and r not in row_all4 and c not in col_all4:
                        if orig[r][c] != 1:
                            new[r][c] = col
    return new