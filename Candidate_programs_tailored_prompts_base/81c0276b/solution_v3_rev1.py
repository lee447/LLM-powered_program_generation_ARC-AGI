import numpy as np
def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_rows = [i for i in range(h) if grid[i].count(grid[i][0])==w and grid[i][0]!=0]
    sep_cols = [j for j in range(w) if all(grid[i][j]==grid[0][j] for i in range(h)) and grid[0][j]!=0]
    sep_rows.sort()
    sep_cols.sort()
    sep_color = grid[sep_rows[0]][0] if sep_rows else None
    bands = []
    prev = -1
    for r in sep_rows:
        if r-prev>1: bands.append((prev+1, r-1))
        prev = r
    if h-prev>1: bands.append((prev+1, h-1))
    zones = []
    prev = -1
    for c in sep_cols:
        if c-prev>1: zones.append((prev+1, c-1))
        prev = c
    if w-prev>1: zones.append((prev+1, w-1))
    counts = {}
    for r0, r1 in bands:
        for c0, c1 in zones:
            if r1-r0<1 or c1-c0<1: continue
            found = None
            for i in range(r0, r1):
                for j in range(c0, c1):
                    c = grid[i][j]
                    if c!=0 and c!=sep_color and grid[i][j+1]==c and grid[i+1][j]==c and grid[i+1][j+1]==c:
                        found = c
                        break
                if found is not None: break
            if found is not None:
                counts[found] = counts.get(found,0) + 1
    items = sorted(counts.items(), key=lambda x: x[1])
    colors, vals = zip(*items) if items else ([],[])
    N = len(colors)
    M = len(zones)
    out = [[0]*M for _ in range(N)]
    for i, c in enumerate(colors):
        for j in range(min(vals[i], M)):
            out[i][j] = c
    return out