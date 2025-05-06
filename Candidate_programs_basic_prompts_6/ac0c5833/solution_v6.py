def solve(grid):
    H, W = len(grid), len(grid[0])
    y_coords = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 4]
    row_counts = {}
    for r, c in y_coords:
        row_counts[r] = row_counts.get(r, 0) + 1
    max_row_count = max(row_counts.values()) if row_counts else 0
    row_anchors = [r for r, ct in row_counts.items() if ct == max_row_count]
    row_anchors.sort()
    red_coords = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 2]
    if not red_coords or not row_anchors:
        return [row[:] for row in grid]
    red_rows = set(r for r, c in red_coords)
    orig_anchor = None
    for r in row_anchors:
        if r in red_rows:
            orig_anchor = r
            break
    if orig_anchor is None:
        orig_anchor = min(row_anchors, key=lambda r: min(abs(r - rr) for rr in red_rows))
    anchors_in_row = sorted(c for c in range(W) if grid[orig_anchor][c] == 4)
    # find segment of original reds
    seg_index = None
    for i in range(len(anchors_in_row) - 1):
        a, b = anchors_in_row[i], anchors_in_row[i+1]
        if any(a < c < b for rr, c in red_coords if rr == orig_anchor):
            seg_index = i
            break
    if seg_index is None:
        seg_index = 0
    origin_c = anchors_in_row[seg_index]
    drs = [r - orig_anchor for r, c in red_coords]
    dcs = [c - origin_c for r, c in red_coords]
    out = [row[:] for row in grid]
    for ra in row_anchors:
        for a in anchors_in_row[:-1]:
            for dr, dc in zip(drs, dcs):
                rr = ra + dr
                cc = a + dc
                if 0 <= rr < H and 0 <= cc < W and out[rr][cc] == 0:
                    out[rr][cc] = 2
    return out