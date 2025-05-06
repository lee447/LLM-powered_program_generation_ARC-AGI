from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows = []
    prev = None
    for r in grid:
        if prev is None or r != prev:
            rows.append(r)
            prev = r
    cols = []
    prevc = None
    for j in range(len(rows[0])):
        col = tuple(r[j] for r in rows)
        if prevc is None or col != prevc:
            cols.append(j)
            prevc = col
    return [[r[j] for j in cols] for r in rows]