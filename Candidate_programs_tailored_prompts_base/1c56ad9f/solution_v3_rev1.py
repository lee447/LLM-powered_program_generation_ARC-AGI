def solve(grid):
    R, C = len(grid), len(grid[0])
    colors = {v for row in grid for v in row if v != 0}
    if len(colors) != 1:
        return grid
    c = colors.pop()
    row_counts = [row.count(c) for row in grid]
    max_count = max(row_counts)
    hbars = [i for i, cnt in enumerate(row_counts) if cnt == max_count]
    if len(hbars) < 2:
        return grid
    top, bottom = hbars[0], hbars[-1]
    vbars = [j for j in range(C) if all(grid[r][j] == c for r in range(top, bottom + 1))]
    out = [[0] * C for _ in range(R)]
    wave = [-1, 0, 1, 0]
    for r in range(R):
        for j in range(C):
            if grid[r][j] != c:
                continue
            if r not in hbars and j not in vbars:
                continue
            s = (r - top - 1) % 4
            j2 = j + wave[s]
            if 0 <= j2 < C:
                out[r][j2] = c
    return out