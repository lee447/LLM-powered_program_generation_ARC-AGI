def solve(grid):
    H, W = len(grid), len(grid[0])
    block = grid[0][0]
    bw = next(c for c in range(W) if grid[0][c] != block)
    stripes = [r for r in range(H) if all(grid[r][c] == block for c in range(bw))]
    stripes.sort()
    bands = [(stripes[i]+1, list(range(stripes[i]+1, stripes[i+1]))) for i in range(len(stripes)-1) if stripes[i]+1<stripes[i+1]]
    ra0 = min(c for r in range(H) for c in range(bw, W) if grid[r][c]!=0)
    shapes = []
    for start, rows in bands:
        coords = [(r, c) for r in rows for c in range(ra0, W) if grid[r][c]!=0]
        cs = [c for _,c in coords]
        minc, maxc = min(cs), max(cs)
        cells = [(r-rows[0], c-minc, grid[r][c]) for r,c in coords]
        shapes.append({'start':rows[0],'w':maxc-minc+1,'cells':cells,'color':cells[0][2]})
    B = len(shapes)
    cols = [s['color'] for s in shapes]
    asc = all(cols[i]<cols[i+1] for i in range(B-1))
    desc = all(cols[i]>cols[i+1] for i in range(B-1))
    out = [[block]*bw for _ in range(H)]
    for i, shp in enumerate(shapes):
        if asc:
            d = shapes[(i+1)%B]
        elif desc:
            d = shapes[B-1-i]
        else:
            d = shapes[(i+1)%B]
        lp = (bw - d['w'])//2
        for dr, dc, v in d['cells']:
            out[shp['start']+dr][lp+dc] = v
    return out