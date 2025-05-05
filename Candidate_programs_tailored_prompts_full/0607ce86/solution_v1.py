def solve(grid):
    H = len(grid)
    W = len(grid[0]) if H else 0
    # find stripe width
    length_counts = {}
    for r in range(H):
        c = 0
        while c < W:
            if grid[r][c] != 0:
                start = c
                while c+1 < W and grid[r][c+1] != 0:
                    c += 1
                length = c - start + 1
                if length > 1:
                    length_counts[length] = length_counts.get(length, 0) + 1
            c += 1
    if not length_counts:
        return [[0]*W for _ in range(H)]
    stripeWidth = max(length_counts, key=length_counts.get)
    # collect runs
    runs = []
    starts = set()
    for r in range(H):
        c = 0
        while c < W:
            if grid[r][c] != 0:
                start = c
                while c+1 < W and grid[r][c+1] != 0:
                    c += 1
                if c - start + 1 == stripeWidth:
                    p = tuple(grid[r][start:start+stripeWidth])
                    runs.append((r, start, p))
                    starts.add(start)
            c += 1
    starts = sorted(starts)
    # build multi-template
    multiTpl = {}
    for s in starts:
        tpl = []
        for j in range(stripeWidth):
            cnt = {}
            for (r, start, p) in runs:
                if start == s:
                    v = p[j]
                    cnt[v] = cnt.get(v, 0) + 1
            best = None
            bc = -1
            for v, k in cnt.items():
                if k > bc:
                    bc = k
                    best = v
            tpl.append(best if best is not None else 0)
        multiTpl[s] = tpl
    # identify bar rows
    barRows = set()
    for (r, s, p) in runs:
        cnt = {}
        for v in p:
            cnt[v] = cnt.get(v, 0) + 1
        if max(cnt.values()) >= stripeWidth - 1:
            barRows.add(r)
    # build bar-template
    barTpl = {}
    if barRows:
        for s in starts:
            # gather bar-run patterns
            barruns = [p for (r, start, p) in runs if r in barRows and start == s]
            if not barruns:
                continue
            tpl = []
            for j in range(stripeWidth):
                cnt = {}
                for p in barruns:
                    if p[j] != multiTpl[s][j]:
                        cnt[p[j]] = cnt.get(p[j], 0) + 1
                best = None
                bc = -1
                for v, k in cnt.items():
                    if k > bc:
                        bc = k
                        best = v
                tpl.append(best if best is not None else multiTpl[s][j])
            barTpl[s] = tpl
    # fill output
    out = [[0]*W for _ in range(H)]
    for (r, s, p) in runs:
        m = multiTpl[s]
        dm = 0
        for j in range(stripeWidth):
            if p[j] != m[j]:
                dm += 1
        chosen = m
        if s in barTpl:
            b = barTpl[s]
            db = 0
            for j in range(stripeWidth):
                if p[j] != b[j]:
                    db += 1
            if db < dm:
                chosen = b
        for j in range(stripeWidth):
            out[r][s+j] = chosen[j]
    return out