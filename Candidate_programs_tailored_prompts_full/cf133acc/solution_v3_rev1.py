from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    hz = []
    for i in range(h):
        runs = 0
        last = 0
        for j in range(w):
            if grid[i][j] != 0:
                last += 1
            else:
                if last >= 3:
                    runs += 1
                last = 0
        if last >= 3:
            runs += 1
        if runs > 0:
            hz.append(i)
    for i in hz:
        row = grid[i]
        cols = {}
        for j,c in enumerate(row):
            if c != 0:
                cols.setdefault(c, []).append(j)
        for c, js in cols.items():
            lo, hi = min(js), max(js)
            for j in range(lo, hi+1):
                out[i][j] = c
    # fill above first horizontal
    if hz:
        r0 = hz[0]
        row0 = out[r0]
        gaps = [j for j in range(w) if grid[r0][j] == 0 and row0[j] != 0]
        for j in gaps:
            c = row0[j]
            for i in range(0, r0):
                if out[i][j] == 0:
                    out[i][j] = c
    # fill vertical drops from each horizontal gap down to next existing
    for i in hz:
        rowi = out[i]
        gaps = [j for j in range(w) if grid[i][j] == 0 and rowi[j] != 0]
        for j in gaps:
            for i2 in range(i+1, h):
                if grid[i2][j] != 0:
                    out[i2][j] = grid[i2][j]
                    break
    return out