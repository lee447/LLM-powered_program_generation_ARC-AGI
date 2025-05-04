def solve(grid):
    H, W = len(grid), len(grid[0])
    row_counts = [sum(1 for c in range(W) if grid[r][c] == 4) for r in range(H)]
    max_row = max(row_counts)
    th_row = max_row - 1 if max_row > 1 else 1
    rows0 = [r for r, cnt in enumerate(row_counts) if cnt >= th_row]
    row_lines = []
    for r in sorted(rows0):
        if not row_lines or r - row_lines[-1][-1] > 1:
            row_lines.append([r])
        else:
            row_lines[-1].append(r)
    row_lines = [cluster[len(cluster)//2] for cluster in row_lines]
    col_counts = [sum(1 for r in range(H) if grid[r][c] == 4) for c in range(W)]
    max_col = max(col_counts)
    th_col = max_col - 1 if max_col > 1 else 1
    cols0 = [c for c, cnt in enumerate(col_counts) if cnt >= th_col]
    col_lines = []
    for c in sorted(cols0):
        if not col_lines or c - col_lines[-1][-1] > 1:
            col_lines.append([c])
        else:
            col_lines[-1].append(c)
    col_lines = [cluster[len(cluster)//2] for cluster in col_lines]
    if len(row_lines) < 2 or len(col_lines) < 2:
        return grid
    row_lines = sorted(row_lines)
    col_lines = sorted(col_lines)
    cell_rows = [(-1 if i == 0 else row_lines[i-1]) for i in range(len(row_lines)+1)] + [H-1]
    cell_cols = [(-1 if i == 0 else col_lines[i-1]) for i in range(len(col_lines)+1)] + [W-1]
    cell_row_bounds = []
    for i in range(len(row_lines)+1):
        top = cell_rows[i] + 1
        bot = cell_rows[i+1] - 1
        cell_row_bounds.append((top, bot))
    cell_col_bounds = []
    for j in range(len(col_lines)+1):
        left = cell_cols[j] + 1
        right = cell_cols[j+1] - 1
        cell_col_bounds.append((left, right))
    tmpl = None
    ti = tj = -1
    coords = []
    for i in range(len(cell_row_bounds)):
        tr, br = cell_row_bounds[i]
        for j in range(len(cell_col_bounds)):
            lc, rc = cell_col_bounds[j]
            has = []
            for r in range(tr, br+1):
                for c in range(lc, rc+1):
                    if grid[r][c] == 2:
                        has.append((r, c))
            if has:
                tmpl = has
                ti, tj = i, j
                break
        if tmpl:
            break
    if tmpl is None:
        return grid
    tr, br = cell_row_bounds[ti]
    lc, rc = cell_col_bounds[tj]
    pat = [(r - tr, c - lc) for r, c in tmpl]
    out = [row[:] for row in grid]
    for i in range(len(cell_row_bounds)):
        for j in range(len(cell_col_bounds)):
            if (i, j) == (ti, tj):
                continue
            tr, br = cell_row_bounds[i]
            lc, rc = cell_col_bounds[j]
            for dr, dc in pat:
                r0 = tr + dr
                c0 = lc + dc
                if 0 <= r0 < H and 0 <= c0 < W and out[r0][c0] == 0:
                    out[r0][c0] = 2
    return out