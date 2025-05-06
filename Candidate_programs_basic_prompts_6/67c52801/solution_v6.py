def solve(grid):
    h, w = len(grid), len(grid[0])
    base_color = next(c for c in set(grid[-1]) if c != 0)
    base_rows = [r for r in range(h) if any(grid[r][c] == base_color for c in range(w))]
    base_top = min(base_rows)
    shapes = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0 and v != base_color:
                shapes.setdefault(v, []).append((r, c))
    infos = {}
    for color, pts in shapes.items():
        rs = [r for r, _ in pts]; cs = [c for _, c in pts]
        r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
        mask = [(r - r0, c - c0) for r, c in pts]
        infos[color] = (r1 - r0 + 1, c1 - c0 + 1, mask)
    holes = []
    c = 0
    while c < w:
        if grid[base_top][c] == base_color:
            c += 1
        else:
            start = c
            while c < w and grid[base_top][c] != base_color:
                c += 1
            holes.append((start, c - start))
    assigned = []
    used = set()
    for start, length in holes:
        for color, (H, W, mask) in infos.items():
            if color in used: continue
            for h0, w0, m0 in ((H, W, mask), (W, H, [(c, r) for r, c in mask])):
                if w0 == length and h0 <= base_top + 1:
                    assigned.append((color, h0, w0, m0, start))
                    used.add(color)
                    break
            if color in used:
                break
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if out[r][c] != 0 and out[r][c] != base_color:
                out[r][c] = 0
    for color, H, W, mask, start in assigned:
        ro = base_top - H + 1
        co = start
        for dr, dc in mask:
            out[ro + dr][co + dc] = color
    return out