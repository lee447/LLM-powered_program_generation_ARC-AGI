from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    centers = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    holes = []
    exts = []
    for cr, cc in centers:
        for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 0:
                holes.append((nr, nc))
                er, ec = nr+dr, nc+dc
                exts.append((er, ec))
                break
    (r1, c1), (r2, c2) = exts
    br0, br1 = min(r1, r2), max(r1, r2)
    bc0, bc1 = min(c1, c2), max(c1, c2)
    vis = [[False]*w for _ in range(h)]
    q = deque()
    if 0 <= r1 < h and 0 <= c1 < w and grid[r1][c1] == 0:
        q.append((r1, c1))
        vis[r1][c1] = True
    while q:
        r, c = q.popleft()
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if br0 <= nr <= br1 and bc0 <= nc <= bc1:
                if 0 <= nr < h and 0 <= nc < w and not vis[nr][nc] and grid[nr][nc] == 0:
                    vis[nr][nc] = True
                    q.append((nr, nc))
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if vis[r][c]:
                out[r][c] = 4
    for hr, hc in holes:
        out[hr][hc] = 4
    return out