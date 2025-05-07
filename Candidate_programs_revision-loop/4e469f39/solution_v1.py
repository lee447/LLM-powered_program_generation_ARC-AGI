def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in grid]
    boxes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not vis[i][j]:
                q=[(i,j)]; vis[i][j]=1; sr, er, sc, ec = i, i, j, j
                for x,y in q:
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        ni, nj = x+dx, y+dy
                        if 0<=ni<h and 0<=nj<w and not vis[ni][nj] and grid[ni][nj]==5:
                            vis[ni][nj]=1; q.append((ni,nj))
                            sr,er = min(sr,ni), max(er,ni)
                            sc,ec = min(sc,nj), max(ec,nj)
                boxes.append((sr,er,sc,ec))
    out = [row[:] for row in grid]
    for sr,er,sc,ec in boxes:
        for i in range(sr+1,er):
            for j in range(sc+1,ec):
                if out[i][j]==0: out[i][j]=2
        op=None
        for i,j in [(i,j) for i in range(sr,er+1) for j in (sc,ec)] + [(i,j) for i in (sr,er) for j in range(sc,ec+1)]:
            if grid[i][j]==0:
                op=(i,j); break
        if op:
            out[op[0]][op[1]] = 2
    return out