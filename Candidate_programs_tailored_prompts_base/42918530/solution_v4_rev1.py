def solve(grid):
    H = len(grid)
    W = len(grid[0])
    zero_rows = [i for i in range(H) if all(x == 0 for x in grid[i])]
    bands = []
    for i in range(len(zero_rows) - 1):
        if zero_rows[i + 1] - zero_rows[i] > 1:
            bands.append((zero_rows[i] + 1, zero_rows[i + 1] - 1))
    if not bands:
        return grid
    mid = len(bands) // 2
    bstart, bend = bands[mid]
    zero_cols = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    block_cols = []
    for i in range(len(zero_cols) - 1):
        if zero_cols[i + 1] - zero_cols[i] > 1:
            block_cols.append((zero_cols[i] + 1, zero_cols[i + 1] - 1))
    if mid % 2 == 0:
        targets = block_cols
    else:
        targets = [block_cols[0]] if block_cols else []
    res = [row[:] for row in grid]
    for cs, ce in targets:
        color = grid[bstart][cs]
        for r in range(bstart + 1, bend):
            if (r - bstart) % 2 == 1:
                for c in range(cs, ce + 1):
                    res[r][c] = color if (c - cs) % 2 == 0 else 0
            else:
                for c in range(cs, ce + 1):
                    res[r][c] = color
    return res