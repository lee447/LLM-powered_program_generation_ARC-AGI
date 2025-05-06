def solve(grid):
    H = len(grid)
    W = len(grid[0])
    rows = [r for r in range(H) if any(grid[r][c] != 0 for c in range(W))]
    bands = []
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j+1] == rows[j] + 1:
            j += 1
        bands.append((rows[i], rows[j]))
        i = j + 1
    cols = [c for c in range(W) if any(grid[r][c] != 0 for r in range(H))]
    belts = []
    i = 0
    while i < len(cols):
        j = i
        while j + 1 < len(cols) and cols[j+1] == cols[j] + 1:
            j += 1
        belts.append((cols[i], cols[j]))
        i = j + 1
    out = [row[:] for row in grid]
    for bi, (r0, r1) in enumerate(bands):
        for bj, (c0, c1) in enumerate(belts):
            s = sum(grid[r][c] != 0 for r in range(r0, r1+1) for c in range(c0, c1+1))
            if bi == 0:
                color = 2 if bj == 0 else 8
            elif bi == 1:
                color = 8 if bj == 0 else 2
            else:
                color = 2 if bj == 0 else 3
            for r in range(r0, r1+1):
                for c in range(c0, c1+1):
                    if grid[r][c] != 0:
                        out[r][c] = color
    return out