def solve(grid):
    R, C = len(grid), len(grid[0])
    dirs4 = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[False]*C for _ in range(R)]
    regions = []
    for i in range(R):
        for j in range(C):
            if grid[i][j]==1 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                minr, maxr, minc, maxc = i, i, j, j
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    if r<minr: minr = r
                    if r>maxr: maxr = r
                    if c<minc: minc = c
                    if c>maxc: maxc = c
                    for dr,dc in dirs4:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and grid[nr][nc]==1:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                cen = ((minr+maxr)/2, (minc+maxc)/2)
                regions.append((cells, minr, maxr, minc, maxc, cen))
    if not regions:
        return [row[:] for row in grid]
    cr, cc = (R-1)/2.0, (C-1)/2.0
    best = min(regions, key=lambda x: (x[5][0]-cr)**2 + (x[5][1]-cc)**2)
    out = [row[:] for row in grid]
    for cells, minr, maxr, minc, maxc, cen in regions:
        er0, er1 = minr-1, maxr+1
        ec0, ec1 = minc-1, maxc+1
        if cells is best[0] or (cells, minr, maxr, minc, maxc, cen)==best:
            for r in range(er0, er1+1):
                for c in range(ec0, ec1+1):
                    if 0<=r<R and 0<=c<C and grid[r][c]!=1:
                        if r==er0 or r==er1 or c==ec0 or c==ec1:
                            out[r][c] = 2
                        else:
                            dr = min(abs(r-minr), abs(r-maxr))
                            dc = min(abs(c-minc), abs(c-maxc))
                            if dr==0 or dc==0:
                                out[r][c] = 8
                            else:
                                out[r][c] = 6
        else:
            for r in range(er0, er1+1):
                for c in range(ec0, ec1+1):
                    if 0<=r<R and 0<=c<C and grid[r][c]!=1:
                        if r==er0 or r==er1 or c==ec0 or c==ec1:
                            out[r][c] = 2
    return out