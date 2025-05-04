def solve(grid):
    H = len(grid)
    W = len(grid[0])
    res = [row[:] for row in grid]
    v_divs = sorted(c for c in range(W) if all(grid[r][c] == 3 for r in range(H)))
    h_divs = sorted(r for r in range(H) if all(grid[r][c] == 3 for c in range(W)))
    c_starts = [0] + [c + 1 for c in v_divs]
    c_ends = [c for c in v_divs] + [W]
    r_starts = [0] + [r + 1 for r in h_divs]
    r_ends = [r for r in h_divs] + [H]
    B = len(r_starts)
    S = len(c_starts)
    for bi in range(B):
        rs, re = r_starts[bi], r_ends[bi]
        for si in range(S):
            cs, ce = c_starts[si], c_ends[si]
            val = None
            if bi == 0:
                if si == 0: val = 2
                elif si == S - 1: val = 4
            elif bi == B - 1:
                if si == 0: val = 1
                elif si == S - 1: val = 8
            else:
                if 0 < si < S - 1: val = 7
            if val is not None:
                for r in range(rs, re):
                    for c in range(cs, ce):
                        res[r][c] = val
    return res