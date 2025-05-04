def solve(grid):
    h, w = len(grid), len(grid[0])
    headers = [(j, grid[0][j]) for j in range(w) if grid[0][j] != 0]
    headers.sort(key=lambda x: x[0])
    grey = 5
    col_counts = [sum(1 for i in range(h) if grid[i][j] == grey) for j in range(w)]
    pillars = []
    j = 0
    while j+1 < w and len(pillars) < 4:
        if col_counts[j] > 0 and col_counts[j+1] > 0:
            pillars.append((j, j+1))
            j += 2
        else:
            j += 1
    pillars = pillars[:4]
    mapping = list(zip(headers, pillars))
    infos = []
    for (hj, hc), (j0, j1) in mapping:
        cells = [(i, j) for i in range(h) for j in (j0, j1)
                 if grid[i][j] != 0 and grid[i][j] != grey]
        used = set()
        for (i1, j1_), (i2, j2_) in ((a,b) for a in cells for b in cells if a < b):
            if abs(i1-i2)+abs(j1_-j2_) == 1:
                color = grid[i1][j1_]
                orient = 'h' if i1 == i2 else 'v'
                sub = 'L' if j1_ == j0 else 'R'
                infos.append((color, orient, sub))
                used |= {(i1,j1_),(i2,j2_)}
                break
        if len(infos) < len(mapping):
            # fallback: single pixel
            i1, j1_ = cells[0]
            color = grid[i1][j1_]
            orient = 'h'
            sub = 'L' if j1_ == j0 else 'R'
            infos.append((color, orient, sub))
    out_h = 8
    out_w = 2 * len(infos) + (len(infos) - 1)
    out = [[0]*out_w for _ in range(out_h)]
    for color, orient, sub in infos:
        ry = 0 if orient == 'h' else out_h - 2
        cx = 0 if sub == 'L' else out_w - 2
        for dy in (0,1):
            for dx in (0,1):
                out[ry+dy][cx+dx] = color
    return out