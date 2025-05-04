def solve(grid):
    h = len(grid)
    w = len(grid[0])
    region_id = [[-1]*w for _ in range(h)]
    regions = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    rid = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 2 and region_id[i][j] < 0:
                col = grid[i][j]
                q = [(i,j)]
                region_id[i][j] = rid
                mr, Mx, mc, Mx2 = i, i, j, j
                for x,y in q:
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == col and region_id[nx][ny] < 0:
                            region_id[nx][ny] = rid
                            q.append((nx,ny))
                            if nx < mr: mr = nx
                            if nx > Mx: Mx = nx
                            if ny < mc: mc = ny
                            if ny > Mx2: Mx2 = ny
                regions.append((col, mr, Mx, mc, Mx2))
                rid += 1
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2 and not seen[i][j]:
                q = [(i,j)]
                seen[i][j] = True
                cells = [(i,j)]
                for x,y in q:
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 2 and not seen[nx][ny]:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                            cells.append((nx,ny))
                minc = min(c for _,c in cells)
                maxc = max(c for _,c in cells)
                rid0 = None
                for x,y in cells:
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and region_id[nx][ny] >= 0:
                            rid0 = region_id[nx][ny]
                            break
                    if rid0 is not None: break
                clusters.append((rid0, cells, minc, maxc))
    res = [row[:] for row in grid]
    for rid0, cells, minc, maxc in clusters:
        col, mr, Mx, mc, Mx2 = regions[rid0]
        for x,y in cells:
            res[x][y] = col
        width = maxc - minc + 1
        if col < 2:
            new_min = Mx2 - width + 1
        else:
            new_min = mc
        for x,y in cells:
            res[x][new_min + (y - minc)] = 2
    return res