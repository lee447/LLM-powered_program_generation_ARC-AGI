def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_rows = [i for i, row in enumerate(grid) if len(set(row)) == 1 and row[0] != 0]
    sep_rows.sort()
    sep_color = grid[sep_rows[0]][0] if sep_rows else None
    sep_cols_all = []
    for j in range(w):
        col_vals = {grid[i][j] for i in range(h)}
        if len(col_vals) == 1 and grid[0][j] != 0:
            sep_cols_all.append(j)
    sep_cols_all.sort()
    vsep = max(0, len(sep_rows) - 1)
    sep_cols = sep_cols_all[:vsep]
    sep_cols.sort()
    bands = []
    prev = -1
    for r in sep_rows:
        if r - prev > 1:
            bands.append((prev + 1, r - 1))
        prev = r
    if h - prev > 1:
        bands.append((prev + 1, h - 1))
    zones = []
    prev = -1
    for c in sep_cols:
        if c - prev > 1:
            zones.append((prev + 1, c - 1))
        prev = c
    if w - prev > 1:
        zones.append((prev + 1, w - 1))
    if len(zones) >= 2:
        zi = [0, len(zones) - 1]
    else:
        zi = list(range(len(zones)))
    found = set()
    for r0, r1 in bands:
        for z in zi:
            c0, c1 = zones[z]
            for i in range(r0, r1):
                for j in range(c0, c1):
                    c = grid[i][j]
                    if c != 0 and c != sep_color:
                        if grid[i][j+1] == c and grid[i+1][j] == c and grid[i+1][j+1] == c:
                            found.add(c)
                            break
                else:
                    continue
                break
    colors = sorted(found)
    N = len(colors)
    out = [[0]*N for _ in range(N)]
    for i, c in enumerate(colors):
        for j in range(i+1):
            out[i][j] = c
    return out