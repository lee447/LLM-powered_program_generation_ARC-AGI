def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                while stack:
                    y,x = stack.pop()
                    cells.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==1:
                            visited[ny][nx] = True
                            stack.append((ny,nx))
                ys = [y for y,x in cells]; xs = [x for y,x in cells]
                miny, minx = min(ys), min(xs)
                sig = frozenset((y-miny,x-minx) for y,x in cells)
                seed = None
                for y in range(miny, max(ys)+1):
                    for x in range(minx, max(xs)+1):
                        if grid[y][x] > 1:
                            seed = (y-miny, x-minx, grid[y][x])
                comps.append((sig, miny, minx, seed))
    shape_map = {}
    for sig, _, _, seed in comps:
        if seed and sig not in shape_map:
            oy,ox,col = seed
            shape_map[sig] = (oy,ox,col)
    out = [row[:] for row in grid]
    for sig, miny, minx, _ in comps:
        if sig in shape_map:
            oy,ox,col = shape_map[sig]
            y, x = miny+oy, minx+ox
            out[y][x] = col
    return out