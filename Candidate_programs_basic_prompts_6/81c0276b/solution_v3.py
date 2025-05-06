def solve(grid):
    h, w = len(grid), len(grid[0])
    vals = {c for row in grid for c in row if c != 0}
    sep = None
    for c in vals:
        for row in grid:
            if all(x == c for x in row):
                sep = c
                break
        if sep is not None:
            break
    sep_rows = {i for i, row in enumerate(grid) if all(x == sep for x in row)}
    sep_cols = {j for j in range(w) if all(grid[i][j] == sep for i in range(h))}
    row_segs = []
    i = 0
    while i < h:
        if i not in sep_rows:
            j = i
            while j < h and j not in sep_rows:
                j += 1
            row_segs.append((i, j - 1))
            i = j
        else:
            i += 1
    col_segs = []
    j = 0
    while j < w:
        if j not in sep_cols:
            k = j
            while k < w and k not in sep_cols:
                k += 1
            col_segs.append((j, k - 1))
            j = k
        else:
            j += 1
    row_segs = [seg for seg in row_segs if seg[1] - seg[0] + 1 >= 2]
    col_segs = [seg for seg in col_segs if seg[1] - seg[0] + 1 >= 2]
    freq = {}
    for rs, re in row_segs:
        for cs, ce in col_segs:
            found = None
            for ii in range(rs, re + 1):
                for jj in range(cs, ce + 1):
                    c = grid[ii][jj]
                    if c != 0 and c != sep:
                        found = c
                        break
                if found is not None:
                    break
            if found is not None:
                freq[found] = freq.get(found, 0) + 1
    items = sorted(freq.items(), key=lambda kv: kv[1])
    if not items:
        return []
    maxfreq = max(v for _, v in items)
    res = []
    for c, f in items:
        res.append([c] * f + [0] * (maxfreq - f))
    return res