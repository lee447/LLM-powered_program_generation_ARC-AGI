def solve(grid):
    h, w = len(grid), len(grid[0])
    zeros = [all(grid[r][c] == 0 for c in range(w)) for r in range(h)]
    bands = []
    start = None
    for r in range(h):
        if not zeros[r] and start is None:
            start = r
        if zeros[r] and start is not None:
            bands.append((start, r - 1))
            start = None
    if start is not None:
        bands.append((start, h - 1))
    colors = [8, 8, 3]
    out = [row[:] for row in grid]
    for i, (r0, r1) in enumerate(bands):
        pts = [(r, c) for r in range(r0, r1 + 1) for c in range(w) if grid[r][c] == 2]
        cols = sorted({c for _, c in pts})
        j, mx = 0, -1
        for k in range(len(cols) - 1):
            if cols[k+1] - cols[k] > mx:
                mx = cols[k+1] - cols[k]
                j = k
        left_set = set(cols[:j+1])
        right_set = set(cols[j+1:])
        left_pts = [(r, c) for r, c in pts if c in left_set]
        right_pts = [(r, c) for r, c in pts if c in right_set]
        target = right_pts if i % 2 == 0 else left_pts
        nc = colors[i] if i < len(colors) else colors[-1]
        for r, c in target:
            out[r][c] = nc
    return out