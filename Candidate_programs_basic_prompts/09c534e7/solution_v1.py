def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] and not vis[i][j]:
                pts = [(i,j)]
                vis[i][j] = True
                for p in pts:
                    r,c = p
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc] and not vis[nr][nc]:
                            vis[nr][nc] = True
                            pts.append((nr,nc))
                vs = {grid[r][c] for r,c in pts if grid[r][c]!=1}
                if vs:
                    v = vs.pop()
                    rs = [r for r,c in pts]; cs = [c for r,c in pts]
                    mnr, mxr = min(rs), max(rs)
                    mnc, mxc = min(cs), max(cs)
                    if mxr-mnr+1 > 2 and mxc-mnc+1 > 2:
                        for r,c in pts:
                            if mnr<r<mxr and mnc<c<mxc:
                                out[r][c] = v
    return out