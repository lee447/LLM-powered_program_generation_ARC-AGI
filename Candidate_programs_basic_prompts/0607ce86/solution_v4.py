def solve(grid):
    n, m = len(grid), len(grid[0])
    # find first fill row
    r_fill = None
    fill_color = None
    for i in range(n):
        row = grid[i]
        nonzeros = [c for c in row if c != 0]
        if not nonzeros: continue
        colors = set(nonzeros)
        if len(colors) != 1: continue
        color = nonzeros[0]
        # find runs of that color
        runs = []
        start = None
        for j in range(m):
            if row[j] == color:
                if start is None: start = j
            else:
                if start is not None:
                    runs.append((start, j))
                    start = None
        if start is not None:
            runs.append((start, m))
        # require a run length >=3
        if any(e - s >= 3 for s, e in runs):
            r_fill = i
            fill_color = color
            segments = [(s, e) for s, e in runs if e - s >= 1]
            break
    # find first blank after fill
    r_blank = None
    for i in range(r_fill + 1, n):
        ok = True
        for s, e in segments:
            for c in range(s, e):
                if grid[i][c] != 0:
                    ok = False
                    break
            if not ok: break
        if ok:
            r_blank = i
            break
    h = r_blank - r_fill - 1
    # extract templates
    templates = []
    for s, e in segments:
        tpl = []
        for dr in range(h):
            tpl.append(grid[r_fill + 1 + dr][s:e])
        templates.append(tpl)
    # find all fill rows
    fills = []
    for i in range(r_fill, n):
        ok = True
        for s, e in segments:
            for c in range(s, e):
                if grid[i][c] != fill_color:
                    ok = False
                    break
            if not ok: break
        if ok:
            fills.append(i)
    # build output
    out = [[0]*m for _ in range(n)]
    for rf in fills:
        # fill row
        for s, e in segments:
            for c in range(s, e):
                out[rf][c] = fill_color
        # pattern rows
        for dr in range(h):
            r = rf + 1 + dr
            if r >= n: break
            for k, (s, e) in enumerate(segments):
                tpl_row = templates[k][dr]
                for dj, v in enumerate(tpl_row):
                    out[r][s + dj] = v
    return out