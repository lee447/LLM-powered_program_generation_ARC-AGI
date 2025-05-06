def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                color = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==color:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                xs = [x for x,y in cells]
                ys = [y for x,y in cells]
                minx, maxx = min(xs), max(xs)
                miny, maxy = min(ys), max(ys)
                ph, pw = maxx-minx+1, maxy-miny+1
                mask = [[0]*pw for _ in range(ph)]
                for x,y in cells:
                    mask[x-minx][y-miny] = 1
                comps.append((cells, color, tuple(tuple(row) for row in mask)))
    def rotations(mask):
        m = [list(row) for row in mask]
        for _ in range(4):
            yield tuple(tuple(row) for row in m)
            m = list(zip(*m[::-1]))
        m = [row[::-1] for row in mask]
        for _ in range(4):
            yield tuple(tuple(row) for row in m)
            m = list(zip(*m[::-1]))
    pair = None
    n = len(comps)
    for i in range(n):
        for j in range(i+1, n):
            mi = comps[i][2]
            mj = comps[j][2]
            for r in rotations(mi):
                if r == mj:
                    pair = (i, j)
                    break
            if pair:
                break
        if pair:
            break
    res = [row[:] for row in grid]
    if pair:
        i,j = pair
        cells_i, ci, _ = comps[i]
        cells_j, cj, _ = comps[j]
        for x,y in cells_i:
            res[x][y] = cj
        for x,y in cells_j:
            res[x][y] = ci
    return res