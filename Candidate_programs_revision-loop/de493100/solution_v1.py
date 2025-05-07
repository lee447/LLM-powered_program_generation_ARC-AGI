def solve(grid):
    R, C = len(grid), len(grid[0])
    from collections import defaultdict
    # find overlay color C such that its positions form a full rectangle
    pos = {}
    for r in range(R):
        for c in range(C):
            pos.setdefault(grid[r][c], []).append((r,c))
    overlay = None
    for v, lst in pos.items():
        rs = [r for r,_ in lst]; cs = [c for _,c in lst]
        if len(lst) == (max(rs)-min(rs)+1)*(max(cs)-min(cs)+1):
            overlay = v
            break
    # bounding box
    rows = [r for r,c in pos[overlay]]; cols = [c for r,c in pos[overlay]]
    r0, r1 = min(rows), max(rows); c0, c1 = min(cols), max(cols)
    h, w = r1-r0+1, c1-c0+1
    # gather non-overlay submatrices patterns
    pats = defaultdict(int)
    subs = {}
    for i in range(R-h+1):
        for j in range(C-w+1):
            ok = True
            a = []
            for di in range(h):
                row = grid[i+di][j:j+w]
                if overlay in row:
                    ok = False; break
                a.append(tuple(row))
            if not ok: continue
            t = tuple(a)
            pats[t] += 1
            subs[(i,j)] = t
    # pick most frequent pattern
    best = max(pats.items(), key=lambda x: x[1])[0]
    return [list(row) for row in best]