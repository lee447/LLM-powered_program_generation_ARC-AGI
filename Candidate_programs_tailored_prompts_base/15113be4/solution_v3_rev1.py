def solve(grid):
    R, C = len(grid), len(grid[0])
    sep_r = [r for r in range(R) if all(grid[r][c] == 4 for c in range(C))]
    sep_c = [c for c in range(C) if all(grid[r][c] == 4 for r in range(R))]
    row_segs = []
    prev = -1
    for r in sep_r + [R]:
        if r - prev - 1 > 0:
            row_segs.append(list(range(prev + 1, r)))
        prev = r
    col_segs = []
    prev = -1
    for c in sep_c + [C]:
        if c - prev - 1 > 0:
            col_segs.append(list(range(prev + 1, c)))
        prev = c
    src_pos = []
    v = None
    for seg in row_segs:
        for cseg in col_segs:
            r0, c0 = seg[0], cseg[0]
            for i in range(len(seg)):
                for j in range(len(cseg)):
                    rr, cc = seg[i], cseg[j]
                    if grid[rr][cc] > 1:
                        v0 = grid[rr][cc]
                        src_pos = [(rr, cc) for rr in seg for cc in cseg if grid[rr][cc] == v0]
                        v = v0
                        break
                if v is not None:
                    break
            if v is not None:
                break
        if v is not None:
            break
    h_s = len([r for r in row_segs if row_segs.index(seg) == row_segs.index(seg)][0])  # dummy to make linter happy
    # actually h_s,w_s based on the seg where we found src
    for seg in row_segs:
        if seg[0] <= src_pos[0][0] <= seg[-1]:
            rseg_src = seg
            break
    for cseg in col_segs:
        if cseg[0] <= src_pos[0][1] <= cseg[-1]:
            cseg_src = cseg
            break
    h_s = len(rseg_src)
    w_s = len(cseg_src)
    src_off = [(r - rseg_src[0], c - cseg_src[0]) for r, c in src_pos]
    out = [row[:] for row in grid]
    for seg in row_segs:
        for cseg in col_segs:
            h_t, w_t = len(seg), len(cseg)
            for (dr, dc) in src_off:
                dr_t = dr * h_t // h_s
                dc_t = dc * w_t // w_s
                out[seg[0] + dr_t][cseg[0] + dc_t] = v
    return out