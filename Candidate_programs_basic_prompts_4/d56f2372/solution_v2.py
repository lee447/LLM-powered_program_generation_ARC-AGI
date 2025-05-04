def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    # determine which color to extract
    target = None
    for c in (8, 6, 1):
        found = False
        for r in range(h):
            for col in grid[r]:
                if col == c:
                    target = c
                    found = True
                    break
            if found:
                break
        if found:
            break
    if target is None:
        return []
    rmin = h
    rmax = -1
    cmin = w
    cmax = -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] == target:
                if r < rmin: rmin = r
                if r > rmax: rmax = r
                if c < cmin: cmin = c
                if c > cmax: cmax = c
    out = []
    for r in range(rmin, rmax+1):
        row = []
        for c in range(cmin, cmax+1):
            row.append(grid[r][c] if grid[r][c] == target else 0)
        out.append(row)
    return out