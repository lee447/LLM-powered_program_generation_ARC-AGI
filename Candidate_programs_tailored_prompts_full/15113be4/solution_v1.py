def solve(grid):
    h, w = len(grid), len(grid[0])
    rows = [i for i in range(h) if all(cell == 4 for cell in grid[i])]
    cols = [j for j in range(w) if all(grid[i][j] == 4 for i in range(h))]
    r_segs = []
    prev = -1
    for r in rows + [h]:
        if r - prev > 1:
            r_segs.append((prev + 1, r))
        prev = r
    c_segs = []
    prev = -1
    for c in cols + [w]:
        if c - prev > 1:
            c_segs.append((prev + 1, c))
        prev = c
    br, bc = len(r_segs), len(c_segs)
    # detect accent color
    accent = None
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v not in (0, 1, 4):
                accent = v
                break
        if accent is not None:
            break
    # collect accent pixels by block
    from collections import defaultdict
    have = {}
    for bi in range(br):
        rs, re = r_segs[bi]
        for bj in range(bc):
            cs, ce = c_segs[bj]
            pts = []
            for i in range(rs, re):
                for j in range(cs, ce):
                    if grid[i][j] == accent:
                        pts.append((i - rs, j - cs))
            if pts:
                bidx = bi * bc + bj
                have[bidx] = pts
    bw = r_segs[0][1] - r_segs[0][0]
    # infer D for each local row
    D = {}
    for bidx, pts in have.items():
        for r0, c0 in pts:
            if r0 not in D:
                D[r0] = (c0 - bidx) % bw
            else:
                # check consistency
                if D[r0] != (c0 - bidx) % bw:
                    # keep first
                    pass
    # draw missing
    out = [row[:] for row in grid]
    for bi in range(br):
        rs, re = r_segs[bi]
        for bj in range(bc):
            cs, ce = c_segs[bj]
            bidx = bi * bc + bj
            if bidx in have:
                continue
            for r0, d in D.items():
                c0 = (bidx + d) % bw
                out[rs + r0][cs + c0] = accent
    return out