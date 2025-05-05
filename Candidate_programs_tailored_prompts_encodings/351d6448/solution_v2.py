def solve(grid):
    h,len_row = len(grid), len(grid[0])
    motif_rows = sorted({r for r in range(h) for c in range(len_row) if grid[r][c] not in (0,5)})
    shapes = []
    for r in motif_rows:
        cells = [(c, grid[r][c]) for c in range(len_row) if grid[r][c] not in (0,5)]
        cols = [c for c,_ in cells]
        if not cols: continue
        minc = min(cols)
        offsets = tuple(c-minc for c in cols)
        vals = tuple(v for _,v in cells)
        shapes.append({'minc':minc,'offsets':offsets,'vals':vals,'length':len(cols)})
    ps = [s['minc'] for s in shapes]
    is_trans = shapes[0]['offsets']==shapes[1]['offsets'] and shapes[0]['vals']==shapes[1]['vals']
    out = [[0]*len_row for _ in range(3)]
    if is_trans:
        d = ps[1]-ps[0]
        p_next = ps[-1] + d
        for off,val in zip(shapes[0]['offsets'], shapes[0]['vals']):
            c = p_next+off
            if 0<=c<len_row: out[1][c] = val
    else:
        Ls = [s['length'] for s in shapes]
        dL = Ls[1]-Ls[0]
        L_next = Ls[-1] + dL
        d = ps[1]-ps[0]
        p_next = ps[-1] + d
        val = shapes[0]['vals'][0]
        for i in range(L_next):
            c = p_next + i
            if 0<=c<len_row: out[1][c] = val
    return out