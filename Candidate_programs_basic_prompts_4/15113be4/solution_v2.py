def solve(grid):
    n = len(grid)
    m = len(grid[0])
    line_val = 4
    h_lines = [i for i in range(n) if all(grid[i][j] == line_val for j in range(m))]
    v_lines = [j for j in range(m) if all(grid[i][j] == line_val for i in range(n))]
    h_bounds = []
    prev = -1
    for r in sorted(h_lines):
        h_bounds.append((prev + 1, r - 1))
        prev = r
    h_bounds.append((prev + 1, n - 1))
    v_bounds = []
    prev = -1
    for c in sorted(v_lines):
        v_bounds.append((prev + 1, c - 1))
        prev = c
    v_bounds.append((prev + 1, m - 1))
    regions = []
    for rs, re in h_bounds:
        for cs, ce in v_bounds:
            if rs <= re and cs <= ce:
                regions.append((rs, re, cs, ce))
    # find source region
    src = None
    best = -1
    for (rs, re, cs, ce) in regions:
        cnt = {}
        for i in range(rs, re + 1):
            for j in range(cs, ce + 1):
                v = grid[i][j]
                if v not in (0, 1, line_val):
                    cnt[v] = cnt.get(v, 0) + 1
        if cnt:
            v, c = max(cnt.items(), key=lambda x: x[1])
            if c > best:
                best = c
                src = (rs, re, cs, ce, v)
    if not src:
        return grid
    rs, re, cs, ce, sourceColor = src
    # find minimal target region size
    sizes = []
    for (r0, r1, c0, c1) in regions:
        if not (r0 == rs and r1 == re and c0 == cs and c1 == ce):
            h = r1 - r0 + 1
            w = c1 - c0 + 1
            sizes.append((h, w))
    targetH, targetW = min(sizes)
    # compute drops on source region
    top = 1 if all(grid[rs][j] == line_val for j in range(cs, ce + 1)) else 0
    bottom = 1 if all(grid[re][j] == line_val for j in range(cs, ce + 1)) else 0
    left = 1 if all(grid[i][cs] == line_val for i in range(rs, re + 1)) else 0
    right = 1 if all(grid[i][ce] == line_val for i in range(rs, re + 1)) else 0
    ist = rs + top
    ied = re - bottom
    jst = cs + left
    jed = ce - right
    srcH = ied - ist + 1
    srcW = jed - jst + 1
    blockH = srcH // targetH if targetH else 1
    blockW = srcW // targetW if targetW else 1
    mask = set()
    for i in range(ist, ied + 1):
        for j in range(jst, jed + 1):
            if grid[i][j] == sourceColor:
                ni = (i - ist) // blockH
                nj = (j - jst) // blockW
                if 0 <= ni < targetH and 0 <= nj < targetW:
                    mask.add((ni, nj))
    res = [row[:] for row in grid]
    for (r0, r1, c0, c1) in regions:
        if r0 == rs and r1 == re and c0 == cs and c1 == ce:
            continue
        h = r1 - r0 + 1
        w = c1 - c0 + 1
        if h < targetH or w < targetW:
            continue
        best_score = 0
        best_off = None
        for off_r in range(h - targetH + 1):
            for off_c in range(w - targetW + 1):
                s = 0
                for (mi, mj) in mask:
                    if grid[r0 + off_r + mi][c0 + off_c + mj] == 1:
                        s += 1
                if s > best_score:
                    best_score = s
                    best_off = (off_r, off_c)
        if best_score > 0:
            off_r, off_c = best_off
            for (mi, mj) in mask:
                rr = r0 + off_r + mi
                cc = c0 + off_c + mj
                if res[rr][cc] == 1:
                    res[rr][cc] = sourceColor
    return res