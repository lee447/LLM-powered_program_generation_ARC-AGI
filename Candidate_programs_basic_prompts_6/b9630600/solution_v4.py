def solve(grid):
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    bands = []
    inside = False
    for r in range(h):
        if any(grid[r][c] != 0 for c in range(w)):
            if not inside:
                start = r
                inside = True
        else:
            if inside:
                bands.append((start, r - 1))
                inside = False
    if inside:
        bands.append((start, h - 1))
    for start, end in bands:
        if end - start < 2:
            continue
        segs = []
        in_seg = False
        for c in range(w):
            if grid[start][c] != 0:
                if not in_seg:
                    seg_start = c
                    in_seg = True
            else:
                if in_seg:
                    segs.append((seg_start, c - 1))
                    in_seg = False
        if in_seg:
            segs.append((seg_start, w - 1))
        if len(segs) < 2:
            continue
        r1 = start + 1
        r2 = end - 1
        for i in range(len(segs) - 1):
            l_end = segs[i][1]
            r_start = segs[i + 1][0]
            color = grid[start][l_end]
            for c in range(l_end, r_start + 1):
                res[r1][c] = color
                res[r2][c] = color
    return res