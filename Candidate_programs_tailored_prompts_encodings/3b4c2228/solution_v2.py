from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    empty_rows = [i for i in range(h) if all(grid[i][j] == 0 for j in range(w))]
    empty_cols = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    if len(empty_rows) == 2 and len(empty_cols) == 2:
        r1, r2 = sorted(empty_rows)
        c1, c2 = sorted(empty_cols)
        row_segs = [(0, r1), (r1+1, r2), (r2+1, h)]
        col_segs = [(0, c1), (c1+1, c2), (c2+1, w)]
    else:
        def make_segs(n):
            base, rem = divmod(n, 3)
            sizes = [base + (1 if i < rem else 0) for i in range(3)]
            segs = []
            start = 0
            for s in sizes:
                segs.append((start, start + s))
                start += s
            return segs
        row_segs = make_segs(h)
        col_segs = make_segs(w)
    out = [[0]*3 for _ in range(3)]
    seen = set()
    for i in range(h-1):
        for j in range(w-1):
            v = grid[i][j]
            if v in (2,3) and grid[i+1][j] == v and grid[i][j+1] == v and grid[i+1][j+1] == v:
                zr = zc = None
                for zi, (rs, re) in enumerate(row_segs):
                    if i >= rs and i+1 < re:
                        zr = zi
                        break
                for zj, (cs, ce) in enumerate(col_segs):
                    if j >= cs and j+1 < ce:
                        zc = zj
                        break
                if zr is not None and zr == zc:
                    seen.add(zr)
    for d in seen:
        out[d][d] = 1
    return out