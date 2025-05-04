def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != bg and not visited[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                rmin = i; rmax = i; cmin = j; cmax = j
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    if r<rmin: rmin = r
                    if r>rmax: rmax = r
                    if c<cmin: cmin = c
                    if c>cmax: cmax = c
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr, c+dc
                        if 0<=rr<h and 0<=cc<w and not visited[rr][cc] and grid[rr][cc]==col:
                            visited[rr][cc] = True
                            stack.append((rr,cc))
                height = rmax - rmin + 1
                width = cmax - cmin + 1
                area = height * width
                comps.append((area, rmin, cmin, height, width, col, cells))
    comps.sort(reverse=True, key=lambda x: x[0])
    maxh = max(c[3] for c in comps)
    maxw = max(c[4] for c in comps)
    out = [[comps[0][5]]*maxw for _ in range(maxh)]
    for _, rmin, cmin, height, width, col, cells in comps[1:]:
        for r,c in cells:
            dr = r - rmin
            dc = c - cmin
            if 0 <= dr < maxh and 0 <= dc < maxw:
                out[dr][dc] = col
    return out