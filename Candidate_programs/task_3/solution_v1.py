def solve(grid):
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    seen = [[False]*W for _ in range(H)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] > 0 and not seen[i][j]:
                pts = []
                stack = [(i,j)]
                seen[i][j] = True
                while stack:
                    r,c = stack.pop()
                    pts.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] > 0 and not seen[nr][nc]:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                color_pts = [(r,c) for (r,c) in pts if grid[r][c] > 1]
                if len(color_pts) == 1:
                    cr, cc = color_pts[0]
                    minr = min(r for r,c in pts)
                    maxr = max(r for r,c in pts)
                    minc = min(c for r,c in pts)
                    maxc = max(c for r,c in pts)
                    # horizontal reflection
                    if minc < maxc:
                        rc = minc + maxc - cc
                        if out[cr][rc] == 1:
                            out[cr][rc] = grid[cr][cc]
                    # vertical reflection
                    if minr < maxr:
                        rr = minr + maxr - cr
                        if out[rr][cc] == 1:
                            out[rr][cc] = grid[cr][cc]
    return out