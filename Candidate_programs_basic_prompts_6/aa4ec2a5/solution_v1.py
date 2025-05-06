def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    vis = [[False]*w for _ in range(h)]
    ccs = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not vis[i][j]:
                stack = [(i,j)]
                vis[i][j] = True
                cc = []
                while stack:
                    r,c = stack.pop()
                    cc.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]==1 and not vis[nr][nc]:
                            vis[nr][nc] = True
                            stack.append((nr,nc))
                ccs.append(cc)
    out = [row[:] for row in grid]
    for cc in ccs:
        rs = [r for r,c in cc]
        cs = [c for r,c in cc]
        minr, maxr = min(rs), max(rs)
        minc, maxc = min(cs), max(cs)
        area = (maxr-minr+1)*(maxc-minc+1)
        if area == len(cc):
            for r,c in cc:
                if r==minr or r==maxr or c==minc or c==maxc:
                    out[r][c] = 2
                else:
                    out[r][c] = 1
        else:
            for r in range(minr, maxr+1):
                for c in range(minc, maxc+1):
                    if r==minr or r==maxr or c==minc or c==maxc:
                        out[r][c] = 2
                    elif r==minr+1 or r==maxr-1 or c==minc+1 or c==maxc-1:
                        out[r][c] = 8
                    else:
                        out[r][c] = 6
    return out