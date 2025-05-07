def solve(grid):
    h, w = len(grid), len(grid[0])
    twos = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 2]
    if not twos:
        return [row[:] for row in grid]
    # find largest connected component of 2's
    seen = [[False]*w for _ in range(h)]
    comps = []
    for y, x in twos:
        if not seen[y][x]:
            stack = [(y, x)]
            comp = []
            seen[y][x] = True
            while stack:
                cy, cx = stack.pop()
                comp.append((cy, cx))
                for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                    ny, nx = cy+dy, cx+dx
                    if 0 <= ny < h and 0 <= nx < w and not seen[ny][nx] and grid[ny][nx] == 2:
                        seen[ny][nx] = True
                        stack.append((ny, nx))
            comps.append(comp)
    twos0 = max(comps, key=len)
    # find pivot 4
    def sgn(v):
        return 1 if v>0 else -1 if v<0 else 0
    pivot = None
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 4:
                dys = [ty - y for ty, tx in twos0]
                dxs = [tx - x for ty, tx in twos0]
                sd = {sgn(d) for d in dys}
                sx = {sgn(d) for d in dxs}
                if len(sd)==1 and len(sx)==1 and 0 not in sd and 0 not in sx:
                    pivot = (y, x)
                    break
        if pivot is not None:
            break
    if pivot is None:
        return [row[:] for row in grid]
    py, px = pivot
    M = [(ty-py, tx-px) for ty, tx in twos0]
    out = [row[:] for row in grid]
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 4:
                for dy, dx in M:
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < h and 0 <= nx < w:
                        out[ny][nx] = 2
    return out