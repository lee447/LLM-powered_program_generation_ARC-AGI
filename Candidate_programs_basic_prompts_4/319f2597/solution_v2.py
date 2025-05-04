from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    zero_rows = set()
    zero_cols = set()
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    zr = sorted(zero_rows)
    zc = sorted(zero_cols)
    r0, r1 = zr[0], zr[1]
    c0, c1 = zc[0], zc[1]
    out = []
    for i, row in enumerate(grid):
        if i == r0 or i == r1:
            new = [v if v == 2 else 0 for v in row]
        else:
            new = [(v if (j in (c0, c1) and v == 2) else (row[j] if j not in (c0, c1) else 0)) for j, v in enumerate(row)]
        out.append(new)
    return out