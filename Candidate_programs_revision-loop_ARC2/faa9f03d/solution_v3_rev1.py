from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    counts = {}
    for r in range(h):
        for c in range(w):
            v = orig[r][c]
            if v:
                counts[v] = counts.get(v, 0) + 1
    cols = sorted(counts.items(), key=lambda x: -x[1])
    B = cols[0][0]
    S = cols[1][0] if len(cols) > 1 else None
    cand = sorted(c for c in counts if c != B)
    # fill-gap for all non-border colors
    for X in cand:
        for r in range(h):
            for c in range(w-2):
                if grid[r][c] == X and grid[r][c+2] == X and grid[r][c+1] != X:
                    grid[r][c+1] = X
        for c in range(w):
            for r in range(h-2):
                if grid[r][c] == X and grid[r+2][c] == X and grid[r+1][c] != X:
                    grid[r+1][c] = X
    # identify hole colors
    hole_colors = [c for c in counts if c not in (B, S)]
    # hole fill
    for hcol in hole_colors:
        cnt = counts[hcol]
        tgt = B if cnt > 1 else S
        for r in range(h):
            for c in range(w):
                if grid[r][c] == hcol:
                    grid[r][c] = tgt
    if hole_colors:
        # scan orig for border arms
        # horizontal
        best = (0, 0, 0)
        for r in range(h):
            c0 = 0
            while c0 < w:
                if orig[r][c0] == B:
                    c1 = c0
                    while c1+1 < w and orig[r][c1+1] == B:
                        c1 += 1
                    length = c1 - c0 + 1
                    if length > best[0]:
                        best = (length, r, c0, c1)
                    c0 = c1+1
                else:
                    c0 += 1
        _, r_max, h_start, h_end = best
        # vertical
        best = (0, 0, 0)
        for c in range(w):
            r0 = 0
            while r0 < h:
                if orig[r0][c] == B:
                    r1 = r0
                    while r1+1 < h and orig[r1+1][c] == B:
                        r1 += 1
                    length = r1 - r0 + 1
                    if length > best[0]:
                        best = (length, c, r0, r1)
                    r0 = r1+1
                else:
                    r0 += 1
        _, c_max, v_start, v_end = best
        # trim extraneous vertical beyond corner
        ext_dir_v = -1 if v_start < r_max else 1
        extr_dir_v = -ext_dir_v
        rr = r_max + extr_dir_v
        while 0 <= rr < h and grid[rr][c_max] == B:
            grid[rr][c_max] = 0
            rr += extr_dir_v
        # extend vertical
        rr = v_start + ext_dir_v
        while 0 <= rr < h:
            if grid[rr][c_max] == B:
                rr += ext_dir_v
                continue
            grid[rr][c_max] = B
            rr += ext_dir_v
        # trim extraneous horizontal beyond corner
        ext_dir_h = -1 if h_start < c_max else 1
        extr_dir_h = -ext_dir_h
        cc = c_max + extr_dir_h
        while 0 <= cc < w and grid[r_max][cc] == B:
            grid[r_max][cc] = 0
            cc += extr_dir_h
    # final fill-gap for small
    if S is not None:
        for r in range(h):
            for c in range(w-2):
                if grid[r][c] == S and grid[r][c+2] == S and grid[r][c+1] != S:
                    grid[r][c+1] = S
        for c in range(w):
            for r in range(h-2):
                if grid[r][c] == S and grid[r+2][c] == S and grid[r+1][c] != S:
                    grid[r+1][c] = S
    return grid