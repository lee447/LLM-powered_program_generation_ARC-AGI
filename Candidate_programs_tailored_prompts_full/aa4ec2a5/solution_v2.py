def solve(grid):
    H, W = len(grid), len(grid[0])
    orig = grid
    out = [row[:] for row in orig]
    visited = [[False]*W for _ in range(H)]
    regions = []
    for r in range(H):
        for c in range(W):
            if orig[r][c]==1 and not visited[r][c]:
                q = [(r,c)]
                visited[r][c] = True
                cells = [(r,c)]
                while q:
                    rr, cc = q.pop()
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0<=nr<H and 0<=nc<W and not visited[nr][nc] and orig[nr][nc]==1:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                            cells.append((nr,nc))
                rs = [x for x,y in cells]; cs = [y for x,y in cells]
                regions.append((min(rs), max(rs), min(cs), max(cs)))
    cmap = {1:6, 2:8, 3:2}
    for r0, r1, c0, c1 in regions:
        for r in range(max(0,r0-3), min(H, r1+4)):
            for c in range(max(0,c0-3), min(W, c1+4)):
                if orig[r][c] in (1,4): continue
                dy = 0 if r0<=r<=r1 else (r0-r if r<r0 else r-r1)
                dx = 0 if c0<=c<=c1 else (c0-c if c<c0 else c-c1)
                d = max(dx, dy)
                if 1 <= d <= 3:
                    out[r][c] = cmap[d]
    return out