def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row.copy() for row in grid]
    vis = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not vis[i][j]:
                stk = [(i,j)]
                vis[i][j] = True
                comp = []
                while stk:
                    r,c = stk.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not vis[nr][nc] and grid[nr][nc]==1:
                            vis[nr][nc] = True
                            stk.append((nr,nc))
                comps.append(comp)
    for comp in comps:
        rs = [r for r,c in comp]; cs = [c for r,c in comp]
        minr, maxr = min(rs), max(rs)
        minc, maxc = min(cs), max(cs)
        # draw border
        for r in range(minr-1, maxr+2):
            for c in (minc-1, maxc+1):
                if 0<=r<h and 0<=c<w:
                    out[r][c] = 2
        for c in range(minc-1, maxc+2):
            for r in (minr-1, maxr+1):
                if 0<=r<h and 0<=c<w:
                    out[r][c] = 2
        # check full rect
        full = True
        for r in range(minr, maxr+1):
            for c in range(minc, maxc+1):
                if grid[r][c] != 1:
                    full = False
                    break
            if not full: break
        if full: continue
        # fill interior
        for r in range(minr, maxr+1):
            for c in range(minc, maxc+1):
                d = min(r-minr, maxr-r, c-minc, maxc-c)
                out[r][c] = 8 if d==0 else 6
    return out