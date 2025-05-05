def solve(grid):
    H, W = len(grid), len(grid[0])
    block_color = grid[0][0]
    bw = 0
    for c in range(W):
        if grid[0][c] == block_color:
            bw += 1
        else:
            break
    shape_min_col = W
    for r in range(H):
        for c in range(bw, W):
            if grid[r][c] != 0 and c < shape_min_col:
                shape_min_col = c
    ra0 = shape_min_col
    stripes = [r for r in range(H) if all(grid[r][c] == block_color for c in range(bw))]
    stripes.sort()
    bands = []
    for i in range(len(stripes)-1):
        a, b = stripes[i]+1, stripes[i+1]
        if a < b:
            bands.append((a, list(range(a, b))))
    shapes = []
    for band_start, rows in bands:
        coords = [(r, c) for r in rows for c in range(ra0, W) if grid[r][c] != 0]
        cs = [c for _,c in coords]
        minc, maxc = min(cs), max(cs)
        cells = [(r-rows[0], c-minc, grid[r][c]) for r,c in coords]
        shapes.append({'start':rows[0], 'w':maxc-minc+1, 'cells':cells})
    out = [[block_color]*bw for _ in range(H)]
    B = len(shapes)
    for i, shp in enumerate(shapes):
        d = shapes[(i+1)%B]
        lp = (bw - d['w'])//2
        for dr, dc, v in d['cells']:
            out[shp['start']+dr][lp+dc] = v
    return out