def solve(grid):
    H, W = len(grid), len(grid[0])
    hr = sorted(r for r in range(H) if all(grid[r][c] == 3 for c in range(W)))
    hc = sorted(c for c in range(W) if all(grid[r][c] == 3 for r in range(H)))
    rowbands = []
    prev = -1
    for sep in hr:
        if sep - prev > 1:
            rowbands.append((prev + 1, sep - 1))
        prev = sep
    if prev < H - 1:
        rowbands.append((prev + 1, H - 1))
    colbands = []
    prev = -1
    for sep in hc:
        if sep - prev > 1:
            colbands.append((prev + 1, sep - 1))
        prev = sep
    if prev < W - 1:
        colbands.append((prev + 1, W - 1))
    rb, cb = len(rowbands), len(colbands)
    for i, (rs, re) in enumerate(rowbands):
        for j, (cs, ce) in enumerate(colbands):
            if i == 0 and j == 0:
                color = 2
            elif i == 0 and j == cb - 1:
                color = 4
            elif i == rb - 1 and j == 0:
                color = 1
            elif i == rb - 1 and j == cb - 1:
                color = 8
            elif 0 < i < rb - 1 and 0 < j < cb - 1:
                color = 7
            else:
                continue
            for r in range(rs, re + 1):
                for c in range(cs, ce + 1):
                    grid[r][c] = color
    return grid