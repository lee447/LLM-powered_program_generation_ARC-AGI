def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import Counter
    cnt = Counter(grid[r][c] for r in range(h) for c in range(w) if grid[r][c] != 0)
    shape_col = next(c for c, k in cnt.items() if k > 1)
    singles = [c for c, k in cnt.items() if k == 1]
    # bounding box of the shape
    rs = [r for r in range(h) for c in range(w) if grid[r][c] == shape_col]
    cs = [c for r in range(h) for c in range(w) if grid[r][c] == shape_col]
    r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
    bh, bw = r1 - r0 + 1, c1 - c0 + 1
    mask = [[grid[r0 + i][c0 + j] == shape_col for j in range(bw)] for i in range(bh)]
    center_r, center_c = (r0 + r1) / 2, (c0 + c1) / 2
    out = [row[:] for row in grid]
    for tcol in singles:
        tr, tc = next((r, c) for r in range(h) for c in range(w) if grid[r][c] == tcol)
        dr, dc = abs(tr - center_r), abs(tc - center_c)
        h_flip, v_flip = dc > dr, dr > dc
        # transform mask
        m2 = [row[:] for row in mask]
        if v_flip:
            m2 = m2[::-1]
        if h_flip:
            m2 = [row[::-1] for row in m2]
        # stamp
        for i in range(bh):
            for j in range(bw):
                if m2[i][j]:
                    nr = int(tr - center_r + (r0 + i))
                    nc = int(tc - center_c + (c0 + j))
                    if 0 <= nr < h and 0 <= nc < w:
                        out[nr][nc] = tcol
    return out