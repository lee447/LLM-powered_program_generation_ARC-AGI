def solve(grid):
    h=len(grid); w=len(grid[0])
    band_cols=[c for c in range(w) if any(grid[r][c]==6 for r in range(h))]
    if not band_cols: return grid
    band_start=min(band_cols); band_end=max(band_cols)
    cluster={1,2,3,4}
    res=[row[:] for row in grid]
    vis=[[False]*w for _ in range(h)]
    from collections import deque
    for y in range(h):
        for x in range(w):
            if not vis[y][x] and grid[y][x] in cluster:
                q=deque([(y,x)]); comp=[]
                vis[y][x]=True
                while q:
                    yy,xx=q.popleft(); comp.append((yy,xx))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx=yy+dy, xx+dx
                        if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and grid[ny][nx] in cluster:
                            vis[ny][nx]=True; q.append((ny,nx))
                if any(xx+1 in band_cols for yy,xx in comp):
                    for yy,xx in comp:
                        if xx<band_start:
                            nx=band_end+(band_start-xx)
                            if 0<=nx<w:
                                res[yy][nx]=grid[yy][xx]
    return res