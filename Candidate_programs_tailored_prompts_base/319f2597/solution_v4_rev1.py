from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    rows = set()
    cols = set()
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == 0:
                rows.add(i)
                cols.add(j)
    rows = sorted(rows)
    cols = sorted(cols)
    k = len(cols)
    out = [row[:] for row in grid]
    for i in rows:
        for j in range(len(out[0])):
            if out[i][j] != k:
                out[i][j] = 0
    for i in range(len(out)):
        if i not in rows:
            for j in cols:
                out[i][j] = 0
    return out