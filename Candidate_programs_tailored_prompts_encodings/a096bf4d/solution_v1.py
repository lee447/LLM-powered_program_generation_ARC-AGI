def solve(grid):
    R, C = len(grid), len(grid[0])
    sep_rows = {r for r in range(R) if all(grid[r][c] == 0 for c in range(C))}
    sep_cols = {c for c in range(C) if all(grid[r][c] == 0 for r in range(R))}
    row_segs = []
    r = 0
    while r < R:
        if r in sep_rows:
            r += 1
        else:
            start = r
            while r < R and r not in sep_rows:
                r += 1
            row_segs.append((start, r))
    col_segs = []
    c = 0
    while c < C:
        if c in sep_cols:
            c += 1
        else:
            start = c
            while c < C and c not in sep_cols:
                c += 1
            col_segs.append((start, c))
    for r0, r1 in row_segs:
        for c0, c1 in col_segs:
            counts = {}
            for i in range(r0, r1):
                for j in range(c0, c1):
                    v = grid[i][j]
                    if v != 0:
                        counts[v] = counts.get(v, 0) + 1
            if not counts:
                continue
            bg = max(counts, key=lambda x: counts[x])
            motif = []
            for i in range(r0, r1):
                for j in range(c0, c1):
                    v = grid[i][j]
                    if v != 0 and v != bg:
                        motif.append((i, j, v))
            if len(motif) < 2:
                continue
            bycol = {}
            for i, j, v in motif:
                bycol.setdefault(v, []).append((i, j))
            major = next(v for v, pts in bycol.items() if len(pts) > 1)
            minor = next(v for v, pts in bycol.items() if len(pts) == 1)
            for i, j in bycol[major]:
                grid[i][j] = minor
    return grid