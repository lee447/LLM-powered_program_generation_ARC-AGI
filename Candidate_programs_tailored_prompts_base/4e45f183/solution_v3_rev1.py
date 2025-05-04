def solve(grid):
    H, W = len(grid), len(grid[0])
    zero_rows = [i for i in range(H) if all(v == 0 for v in grid[i])]
    zero_cols = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    row_intervals = [list(range(zero_rows[i] + 1, zero_rows[i + 1])) for i in range(len(zero_rows) - 1) if zero_rows[i + 1] - zero_rows[i] > 1]
    col_intervals = [list(range(zero_cols[j] + 1, zero_cols[j + 1])) for j in range(len(zero_cols) - 1) if zero_cols[j + 1] - zero_cols[j] > 1]
    R, C = len(row_intervals), len(col_intervals)
    cnt = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v:
                cnt[v] = cnt.get(v, 0) + 1
    items = sorted(cnt.items(), key=lambda x: x[1])
    fg = items[0][0]
    bg = items[-1][0]
    seed_block = None
    for rs in row_intervals:
        for cs in col_intervals:
            pts = [(r, c) for r in rs for c in cs if grid[r][c] == fg]
            if len(pts) > 1:
                minr = min(r for r, c in pts)
                minc = min(c for r, c in pts)
                shape = [(r - minr, c - minc) for r, c in pts]
                h_bb = max(r - minr for r, c in pts) + 1
                w_bb = max(c - minc for r, c in pts) + 1
                seed_block = (rs, cs, shape, h_bb, w_bb)
                break
        if seed_block:
            break
    if not seed_block:
        return grid
    _, _, master_shape, h_bb, w_bb = seed_block
    row_seeds = [[] for _ in range(R)]
    col_seeds = [[] for _ in range(C)]
    for i, rs in enumerate(row_intervals):
        for j, cs in enumerate(col_intervals):
            pts = [(r, c) for r in rs for c in cs if grid[r][c] == fg]
            if pts:
                minr = min(r for r, c in pts)
                minc = min(c for r, c in pts)
                rel = [(r - minr, c - minc) for r, c in pts]
                row_seeds[i].append((j, rel))
                col_seeds[j].append((i, rel))
    out = [row[:] for row in grid]
    for i, rs in enumerate(row_intervals):
        bh = len(rs)
        for j, cs in enumerate(col_intervals):
            bw = len(cs)
            for r in rs:
                for c in cs:
                    if out[r][c] != 0:
                        out[r][c] = bg
            coords = []
            if len(row_seeds[i]) >= 2:
                for _, rel in row_seeds[i]:
                    coords += rel
            elif len(row_seeds[i]) == 1:
                js, rel = row_seeds[i][0]
                shift = int((bw - w_bb) * (j - js) / max(C - 1, 1) + 0.5)
                for dr, dc in rel:
                    coords.append((dr, dc + shift))
            else:
                if len(col_seeds[j]) >= 2:
                    for _, rel in col_seeds[j]:
                        coords += rel
                elif len(col_seeds[j]) == 1:
                    is_, rel = col_seeds[j][0]
                    shift = int((bh - h_bb) * (i - is_) / max(R - 1, 1) + 0.5)
                    for dr, dc in rel:
                        coords.append((dr + shift, dc))
                else:
                    or_, oc = seed_block[0][0], seed_block[1][0]
                    shift_r = int((bh - h_bb) * i / max(R - 1, 1) + 0.5)
                    shift_c = int((bw - w_bb) * j / max(C - 1, 1) + 0.5)
                    for dr, dc in master_shape:
                        coords.append((dr + shift_r, dc + shift_c))
            seen = set()
            for dr, dc in coords:
                if 0 <= dr < bh and 0 <= dc < bw and (dr, dc) not in seen:
                    seen.add((dr, dc))
                    out[rs[0] + dr][cs[0] + dc] = fg
    return out