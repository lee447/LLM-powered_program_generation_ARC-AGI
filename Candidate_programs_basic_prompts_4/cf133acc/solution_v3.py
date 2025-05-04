def solve(grid):
    h, w = len(grid), len(grid[0])
    pos = {}
    for r in range(h):
        for c in range(w):
            x = grid[r][c]
            if x:
                pos.setdefault(x, []).append((r, c))
    stripe_h, stripe_v = [], []
    for x, cells in pos.items():
        rows = {r for r, _ in cells}
        cols = {c for _, c in cells}
        if len(rows) == 1 and len(cols) > 1:
            r = next(iter(rows))
            cs = sorted(cols)
            runs = []
            start = cs[0]
            prev = cs[0]
            for c in cs[1:]:
                if c == prev + 1:
                    prev = c
                else:
                    runs.append((start, prev))
                    start = c; prev = c
            runs.append((start, prev))
            if len(runs) >= 2:
                g0 = runs[0][1] + 1
                g1 = runs[1][0] - 1
                if g0 == g1:
                    stripe_h.append({
                        'color': x, 'row': r,
                        'min_col': runs[0][0], 'max_col': runs[1][1],
                        'gap_col': g0
                    })
                    continue
        if len(cols) == 1:
            c = next(iter(cols))
            rs = sorted(rows)
            if all(rs[i] + 1 == rs[i+1] for i in range(len(rs)-1)):
                stripe_v.append({
                    'color': x, 'col': c,
                    'row_end': rs[-1]
                })
    spines = sorted({s['gap_col'] for s in stripe_h})
    attaches = {C: [] for C in spines}
    for s in stripe_h:
        attaches[s['gap_col']].append({
            'type': 'h', 'color': s['color'],
            'row': s['row'],
            'min_col': s['min_col'], 'max_col': s['max_col']
        })
    for s in stripe_v:
        if s['col'] in attaches:
            attaches[s['col']].append({
                'type': 'v', 'color': s['color'],
                'row_end': s['row_end']
            })
    out = [[0]*w for _ in range(h)]
    for C in spines:
        prev = 0
        lst = sorted(attaches[C], key=lambda a: a['row'] if a['type']=='h' else a['row_end'])
        for a in lst:
            if a['type'] == 'h':
                r = a['row']
                for rr in range(prev, r+1):
                    out[rr][C] = a['color']
                for cc in range(a['min_col'], a['max_col']+1):
                    out[r][cc] = a['color']
                prev = r
            else:
                re = a['row_end']
                for rr in range(prev+1, re+1):
                    out[rr][C] = a['color']
                prev = re
    return out