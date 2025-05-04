from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = 0
    stripe_rows = [i for i in range(h) if len(set(grid[i])) == 1 and grid[i][0] != bg]
    stripe_cols = [j for j in range(w) if len({grid[i][j] for i in range(h)}) == 1 and grid[0][j] != bg]
    stripe_rows.sort()
    stripe_cols.sort()
    row_ranges = []
    r0 = 0
    for sr in stripe_rows:
        row_ranges.append((r0, sr))
        r0 = sr + 1
    if r0 < h:
        row_ranges.append((r0, h))
    col_ranges = []
    c0 = 0
    for sc in stripe_cols:
        col_ranges.append((c0, sc))
        c0 = sc + 1
    if c0 < w:
        col_ranges.append((c0, w))
    R = len(row_ranges)
    C = len(col_ranges)
    brow = [0]*h
    for bi,(a,b) in enumerate(row_ranges):
        for i in range(a,b):
            brow[i] = bi
    bcol = [0]*w
    for bj,(a,b) in enumerate(col_ranges):
        for j in range(a,b):
            bcol[j] = bj
    out = [row[:] for row in grid]
    # collect shapes by color
    shapes = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v != bg and i not in stripe_rows and j not in stripe_cols:
                key = v
                shapes.setdefault(key, set()).add((brow[i], bcol[j]))
    for v, blocks in shapes.items():
        brs = [b[0] for b in blocks]
        bcs = [b[1] for b in blocks]
        min_br, max_br = min(brs), max(brs)
        min_bc, max_bc = min(bcs), max(bcs)
        if max_br > min_br and max_bc > min_bc:
            # rectangle fill
            sr0, sr1 = row_ranges[min_br]
            sc0, sc1 = col_ranges[min_bc]
            bh = sr1 - sr0
            bw = sc1 - sc0
            # gather reference pixels
            ref = [(i - sr0, j - sc0) for i in range(sr0, sr1) for j in range(sc0, sc1) if grid[i][j] == v]
            for br in range(min_br, max_br+1):
                tr0, tr1 = row_ranges[br]
                for bc in range(min_bc, max_bc+1):
                    if (br, bc) in blocks: continue
                    tc0, tc1 = col_ranges[bc]
                    dr_flip = br == max_br
                    dc_flip = bc == max_bc
                    for dr, dc in ref:
                        drr = bh-1-dr if dr_flip else dr
                        dcc = bw-1-dc if dc_flip else dc
                        out[tr0 + drr][tc0 + dcc] = v
        elif len(blocks) == 1:
            # diagonal mirror
            br, bc = next(iter(blocks))
            nbr, nbc = bc, br
            if 0 <= nbr < R and 0 <= nbc < C and (nbr, nbc) not in blocks:
                sr0, sr1 = row_ranges[br]
                sc0, sc1 = col_ranges[bc]
                tr0, tr1 = row_ranges[nbr]
                tc0, tc1 = col_ranges[nbc]
                for i in range(sr0, sr1):
                    for j in range(sc0, sc1):
                        if grid[i][j] == v:
                            out[tr0 + (i - sr0)][tc0 + (j - sc0)] = v
    return out