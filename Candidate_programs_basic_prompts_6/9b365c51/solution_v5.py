def solve(grid):
    H, W = len(grid), len(grid[0])
    bars = sorted(x for x in range(W) if any(grid[r][x] not in (0, 8) for r in range(H)))
    colors = [grid[next(r for r in range(H) if grid[r][c] not in (0, 8))][c] for c in bars]
    seen = [[False]*W for _ in range(H)]
    out = [[0]*W for _ in range(H)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def flood(r,c):
        pts = [(r,c)]
        seen[r][c] = True
        for i in range(len(pts)):
            y,x = pts[i]
            for dy,dx in dirs:
                ny, nx = y+dy, x+dx
                if 0<=ny<H and 0<=nx<W and not seen[ny][nx] and grid[ny][nx]==8:
                    seen[ny][nx]=True
                    pts.append((ny,nx))
        return pts
    seg = bars[1]-bars[0] if len(bars)>1 else W
    for r in range(H):
        for c in range(W):
            if grid[r][c]==8 and not seen[r][c]:
                comp = flood(r,c)
                minc = min(x for _,x in comp)
                for y,x in comp:
                    i = (x-minc)//seg
                    if 0 <= i < len(colors):
                        out[y][x] = colors[i]
    return out