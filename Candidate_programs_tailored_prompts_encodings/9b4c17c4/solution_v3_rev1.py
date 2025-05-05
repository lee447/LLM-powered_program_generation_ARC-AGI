def solve(grid):
    R, C = len(grid), len(grid[0])
    hor = ver = False
    brow = bcol = -1
    for i in range(R - 1):
        if all(grid[i][j] == grid[i + 1][j] for j in range(C)) and grid[i][0] != grid[i + 1][0]:
            hor = True
            brow = i
            break
    if not hor:
        for j in range(C - 1):
            if all(grid[i][j] == grid[i][j + 1] for i in range(R)) and grid[0][j] != grid[0][j + 1]:
                ver = True
                bcol = j
                break
    seen = [[False] * C for _ in range(R)]
    comps = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 2 and not seen[i][j]:
                stack = [(i, j)]
                seen[i][j] = True
                pts = []
                while stack:
                    x, y = stack.pop()
                    pts.append((x, y))
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < R and 0 <= ny < C and not seen[nx][ny] and grid[nx][ny] == 2:
                            seen[nx][ny] = True
                            stack.append((nx, ny))
                rs = [p[0] for p in pts]
                cs = [p[1] for p in pts]
                comps.append((min(rs), max(rs), min(cs), max(cs)))
    out = [[0] * C for _ in range(R)]
    if hor:
        c1 = grid[0][0]
        c2 = grid[brow + 1][0]
        for i in range(R):
            for j in range(C):
                out[i][j] = c1 if i <= brow else c2
    else:
        c1 = grid[0][0]
        c2 = grid[0][bcol + 1]
        for i in range(R):
            for j in range(C):
                out[i][j] = c1 if j <= bcol else c2
    for rmin, rmax, cmin, cmax in comps:
        h = rmax - rmin + 1
        w = cmax - cmin + 1
        if hor:
            in_region1 = (rmax <= brow)
            region_color = c1 if in_region1 else c2
            region_start = 0
            region_end = C - 1
        else:
            in_region1 = (cmax <= bcol)
            region_color = c1 if in_region1 else c2
            region_start = 0 if in_region1 else bcol + 1
            region_end = bcol if in_region1 else C - 1
        if region_color == 1:
            ncmin = region_end - w + 1
        else:
            ncmin = region_start
        for dr in range(h):
            for dc in range(w):
                out[rmin + dr][ncmin + dc] = 2
    return out