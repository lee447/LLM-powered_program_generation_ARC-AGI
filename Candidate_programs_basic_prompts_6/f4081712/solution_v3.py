def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if not seen[i][j]:
                seen[i][j] = True
                col = grid[i][j]
                queue = [(i,j)]
                pts = [(i,j)]
                for x,y in queue:
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<H and 0<=ny<W and not seen[nx][ny] and grid[nx][ny]==col:
                            seen[nx][ny] = True
                            queue.append((nx,ny))
                            pts.append((nx,ny))
                rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                area = (r1-r0+1)*(c1-c0+1)
                if area == len(pts):
                    comps.append((len(pts), col, r0, r1, c0, c1))
    # pick component: not touching border
    cand = [c for c in comps if c[2]>0 and c[3]<H-1 and c[4]>0 and c[5]<W-1]
    if not cand:
        cand = [c for c in comps if c[0]>1]
    comp = sorted(cand, key=lambda x: x[0])[0]
    _, _, r0, r1, c0, c1 = comp
    h, w = r1-r0+1, c1-c0+1
    # try above
    if r0-h >= 0:
        rs, cs = r0-h, r0
        return [row[c0:c1+1] for row in grid[rs:cs]]
    # below
    if r1+h < H:
        rs, cs = r1+1, r1+h+1
        return [row[c0:c1+1] for row in grid[rs:cs]]
    # left
    if c0-w >= 0:
        cs0, cs1 = c0-w, c0
        return [row[cs0:cs1] for row in grid[r0:r1+1]]
    # right
    cs0, cs1 = c1+1, c1+1+w
    return [row[cs0:cs1] for row in grid[r0:r1+1]]