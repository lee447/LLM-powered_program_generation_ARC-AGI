def solve(grid):
    h = len(grid)
    w = len(grid[0])
    sep_cols = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    sep_start = sep_cols[0]
    sep_end = sep_start
    while sep_end + 1 in sep_cols:
        sep_end += 1
    left_w = sep_start
    right_start = sep_end + 1
    left = [row[:left_w] for row in grid]
    right = [row[right_start:] for row in grid]
    sep_rows = [i for i in range(h) if all(v == 0 for v in right[i])]
    groups = []
    for a, b in zip(sep_rows, sep_rows[1:]):
        if b > a + 1:
            groups.append((a + 1, b))
    shape_colors = []
    shape_widths = []
    for top, bot in groups:
        cw = None
        widths = []
        for i in range(top, bot):
            row = right[i]
            cnt = sum(1 for x in row if x != 0)
            if cnt > 0:
                cw = row[row.index(next(x for x in row if x != 0))]
            widths.append(cnt)
        shape_colors.append(cw)
        shape_widths.append(tuple(widths))
    shapes_map = {}
    for c, wts in zip(shape_colors, shape_widths):
        shapes_map.setdefault(wts, []).append(c)
    zeros_widths = []
    for top, bot in groups:
        wts = []
        for i in range(top, bot):
            row = left[i]
            wts.append(sum(1 for x in row if x == 0))
        zeros_widths.append(tuple(wts))
    used = set()
    result = [list(r) for r in left]
    for (top, bot), zw in zip(groups, zeros_widths):
        cands = shapes_map.get(zw, [])
        col = None
        if len(cands) == 1:
            col = cands[0]
        else:
            for x in sorted(cands):
                if x not in used:
                    col = x
                    break
            if col is None and cands:
                col = min(cands)
        if col is None:
            continue
        used.add(col)
        for i in range(top, bot):
            for j in range(left_w):
                if result[i][j] == 0:
                    result[i][j] = col
    return result