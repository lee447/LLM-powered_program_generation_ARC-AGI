def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not seen[i][j]:
                stk = [(i,j)]
                seen[i][j] = True
                pts = []
                while stk:
                    x,y = stk.pop()
                    pts.append((x,y))
                    for dx,dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 1 and not seen[nx][ny]:
                            seen[nx][ny] = True
                            stk.append((nx,ny))
                pts.sort()
                comps.append(pts)
    # gather colors in input in order of first appearance, excluding 0 and 1
    colors = []
    seenc = set()
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v not in (0,1) and v not in seenc:
                seenc.add(v)
                colors.append(v)
    if not colors:
        colors = [2,3]
    nc = len(colors)
    # assign colors symmetrically: for j,color in enumerate(colors):
    #   comps[j] and comps[-j-1] -> color
    assign = [None]*len(comps)
    for idx, c in enumerate(colors):
        if idx < len(comps):
            assign[idx] = c
        if idx < len(comps):
            k = len(comps)-1-idx
            if 0 <= k < len(comps):
                assign[k] = c
    last = colors[-1]
    for i in range(len(assign)):
        if assign[i] is None:
            assign[i] = last
    out = [row[:] for row in grid]
    for comp, col in zip(comps, assign):
        for x,y in comp:
            out[x][y] = col
    return out