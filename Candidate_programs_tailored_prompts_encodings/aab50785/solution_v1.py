def solve(grid):
    h, w = len(grid), len(grid[0])
    bands = []
    for r in range(h-1):
        cols = []
        for c in range(w-1):
            if grid[r][c]==8 and grid[r][c+1]==8 and grid[r+1][c]==8 and grid[r+1][c+1]==8:
                cols.append(c)
        if len(cols)>=2:
            bands.append((r, sorted(cols)))
    if not bands:
        return [[]]
    r0, cols0 = bands[0]
    c1, c2 = cols0[0], cols0[1]
    nb = None
    for r, cols in bands[1:]:
        nb = r
        break
    if nb is None:
        end = r0+2
    else:
        end = nb
    rs, re = r0, end
    cs, ce = c1+2, c2
    out = []
    for r in range(rs, re):
        row = []
        for c in range(cs, ce):
            v = grid[r][c]
            row.append(v if v!=8 else 0)
        out.append(row)
    return out