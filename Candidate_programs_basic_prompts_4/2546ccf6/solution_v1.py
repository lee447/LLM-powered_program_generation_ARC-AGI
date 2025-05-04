def solve(grid):
    h = len(grid)
    w = len(grid[0])
    border_counts = {}
    for r in range(h):
        v = grid[r][0]
        if all(grid[r][c] == v for c in range(w)):
            border_counts[v] = border_counts.get(v, 0) + 1
    for c in range(w):
        v = grid[0][c]
        if all(grid[r][c] == v for r in range(h)):
            border_counts[v] = border_counts.get(v, 0) + 1
    border_color = max(border_counts, key=border_counts.get)
    sep_rows = [r for r in range(h) if all(grid[r][c] == border_color for c in range(w))]
    sep_cols = [c for c in range(w) if all(grid[r][c] == border_color for r in range(h))]
    sep_rows.sort()
    sep_cols.sort()
    row_edges = [-1] + sep_rows + [h]
    col_edges = [-1] + sep_cols + [w]
    row_ranges = [(row_edges[i]+1, row_edges[i+1]) for i in range(len(row_edges)-1)]
    col_ranges = [(col_edges[i]+1, col_edges[i+1]) for i in range(len(col_edges)-1)]
    def block_index(ranges, x):
        for i, (a, b) in enumerate(ranges):
            if a <= x < b:
                return i
    colors = set()
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0 and v != border_color:
                colors.add(v)
    for t in colors:
        cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == t]
        brs = {block_index(row_ranges, r) for r, _ in cells}
        bcs = {block_index(col_ranges, c) for _, c in cells}
        if not brs or not bcs: continue
        rmin, rmax = min(brs), max(brs)
        cmin, cmax = min(bcs), max(bcs)
        if rmax - rmin != 1 or cmax - cmin != 1: continue
        region = {(r, c) for r in (rmin, rmax) for c in (cmin, cmax)}
        counts = {}
        by_block = {}
        for r, c in cells:
            br = block_index(row_ranges, r)
            bc = block_index(col_ranges, c)
            by_block.setdefault((br, bc), []).append((r, c))
        for b, lst in by_block.items():
            counts[b] = len(lst)
        pb = max(counts, key=counts.get)
        pr, pc = pb
        pattern = [(r - row_ranges[pr][0], c - col_ranges[pc][0]) for r, c in by_block[pb]]
        for rr in (rmin, rmax):
            for cc in (cmin, cmax):
                if (rr, cc) not in by_block:
                    rs, _ = row_ranges[rr]
                    cs, _ = col_ranges[cc]
                    for dr, dc in pattern:
                        grid[rs+dr][cs+dc] = t
    return grid