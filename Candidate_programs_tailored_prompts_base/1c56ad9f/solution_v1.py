def solve(grid):
    R, C = len(grid), len(grid[0])
    cols = {v for row in grid for v in row if v != 0}
    if len(cols) != 1:
        return grid
    c = cols.pop()
    if c not in (2, 3):
        return grid
    hbars = [r for r in range(R) if grid[r].count(c) > 1]
    if not hbars:
        return grid
    top, bottom = min(hbars), max(hbars)
    interior = {r for r in hbars if r != top and r != bottom}
    vbars = []
    for j in range(C):
        ok = True
        for r in range(top + 1, bottom):
            if grid[r][j] != c:
                ok = False
                break
        if ok:
            vbars.append(j)
    out = [[0] * C for _ in range(R)]
    for r in range(R):
        for j in range(C):
            if grid[r][j] != c:
                continue
            if r in interior:
                j2 = j + 1
            elif r == top or r == bottom:
                j2 = j
            elif j in vbars:
                dr = r - top
                j2 = j - 1 if dr % 2 else j
            else:
                j2 = j
            if 0 <= j2 < C:
                out[r][j2] = c
    return out