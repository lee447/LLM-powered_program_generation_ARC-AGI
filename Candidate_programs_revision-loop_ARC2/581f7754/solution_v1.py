from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = max({c:0 for row in grid for c in row}, key=lambda c: sum(row.count(c) for row in grid))
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if not vis[i][j] and grid[i][j] != bg:
                col = grid[i][j]
                q = [(i,j)]
                vis[i][j] = True
                cells = []
                for x,y in q:
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]!= bg:
                            vis[nx][ny] = True
                            q.append((nx,ny))
                minr = min(x for x,y in cells)
                maxr = max(x for x,y in cells)
                minc = min(y for x,y in cells)
                maxc = max(y for x,y in cells)
                comps.append((cells, minr, maxr, minc, maxc))
    if h > w:
        axis = 1
    else:
        axis = 0
    centers = []
    for _, r1, r2, c1, c2 in comps:
        centers.append(((r1+r2)//2, (c1+c2)//2)[axis])
    centers.sort()
    tgt = centers[len(centers)//2]
    out = [[bg]*w for _ in range(h)]
    for cells, r1, r2, c1, c2 in comps:
        ctr = ((r1+r2)//2, (c1+c2)//2)[axis]
        d = tgt - ctr
        for x,y in cells:
            nx, ny = (x, y+d) if axis==1 else (x+d, y)
            out[nx][ny] = grid[x][y]
    return out