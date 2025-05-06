def solve(grid):
    h, w = len(grid), len(grid[0])
    hruns = []
    for y in range(h):
        x = 0
        while x < w:
            if grid[y][x] != 0:
                c0 = x
                cols = set()
                while x < w and grid[y][x] != 0:
                    cols.add(grid[y][x])
                    x += 1
                hruns.append({'row': y, 'c1': c0, 'c2': x - 1, 'colors': cols})
            else:
                x += 1
    vruns = []
    for x in range(w):
        y = 0
        while y < h:
            if grid[y][x] != 0:
                r0 = y
                cols = set()
                while y < h and grid[y][x] != 0:
                    cols.add(grid[y][x])
                    y += 1
                vruns.append({'col': x, 'r1': r0, 'r2': y - 1, 'colors': cols})
            else:
                y += 1
    h_frames = [r for r in hruns if len(r['colors']) == 1 and (r['c2'] - r['c1'] + 1) > 1]
    v_frames = [r for r in vruns if len(r['colors']) == 1 and (r['r2'] - r['r1'] + 1) > 1]
    h_pats = [r for r in hruns if len(r['colors']) > 1]
    v_pats = [r for r in vruns if len(r['colors']) > 1]
    out = [row[:] for row in grid]
    if h_pats and v_pats:
        # both expansions
        # horizontal pattern expand over vpattern rows
        vp = max(v_pats, key=lambda r: r['r2'] - r['r1'])
        r0, r1, r2 = vp['r1'], vp['r1'], vp['r2']
        hp_c1 = min(r['c1'] for r in h_pats)
        hp_c2 = max(r['c2'] for r in h_pats)
        patterns = sorted(r['row'] for r in h_pats)
        L = len(patterns)
        for r in range(r1, r2 + 1):
            pr = patterns[(r - r0) % L]
            for c in range(hp_c1, hp_c2 + 1):
                out[r][c] = grid[pr][c]
        # vertical pattern expand over hframe cols
        hf = h_frames[0]
        hf_c1, hf_c2 = hf['c1'], hf['c2']
        vp_col = vp['col']
        for r in range(r1, r2 + 1):
            val = grid[r][vp_col]
            for c in range(hf_c1, hf_c2 + 1):
                out[r][c] = val
    elif h_pats and v_frames:
        # only horizontal pattern expand over vframe rows
        vf = v_frames[0]
        r1, r2 = vf['r1'], vf['r2']
        hp_c1 = min(r['c1'] for r in h_pats)
        hp_c2 = max(r['c2'] for r in h_pats)
        patterns = sorted(r['row'] for r in h_pats)
        L = len(patterns)
        for r in range(r1, r2 + 1):
            pr = patterns[(r - r1) % L]
            for c in range(hp_c1, hp_c2 + 1):
                out[r][c] = grid[pr][c]
    elif v_pats and h_frames:
        # only vertical pattern expand over hframe cols
        hf = h_frames[0]
        c1, c2 = hf['c1'], hf['c2']
        vp = max(v_pats, key=lambda r: r['r2'] - r['r1'])
        r1, r2 = vp['r1'], vp['r2']
        col = vp['col']
        for r in range(r1, r2 + 1):
            val = grid[r][col]
            for c in range(c1, c2 + 1):
                out[r][c] = val
    return out