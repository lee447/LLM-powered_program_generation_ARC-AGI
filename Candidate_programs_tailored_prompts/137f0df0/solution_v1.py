def solve(grid):
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    grey_rows = [r for r in range(H) if any(grid[r][c] == 5 for c in range(W))]
    bands = []
    i = 0
    while i < len(grey_rows):
        if i+1 < len(grey_rows) and grey_rows[i+1] == grey_rows[i] + 1:
            bands.append((grey_rows[i], grey_rows[i+1]))
            i += 2
        else:
            i += 1
    all_grey_cols = sorted({c for r in grey_rows for c in range(W) if grid[r][c] == 5})
    min_g, max_g = all_grey_cols[0], all_grey_cols[-1]
    stripe_cols = set()
    for b0, b1 in bands:
        cols = sorted({c for c in range(W) if grid[b0][c] == 5 or grid[b1][c] == 5})
        runs = []
        start = cols[0]
        prev = cols[0]
        for c in cols[1:]:
            if c == prev + 1:
                prev = c
            else:
                runs.append((start, prev))
                start = c
                prev = c
        runs.append((start, prev))
        for i in range(len(runs) - 1):
            for c in range(runs[i][1] + 1, runs[i+1][0]):
                out[b0][c] = 2
                out[b1][c] = 2
                stripe_cols.add(c)
    first_end = bands[0][1]
    last_start = bands[-1][0]
    for r in range(first_end + 1, last_start):
        if all(grid[r][c] == 0 for c in range(W)):
            for c in range(min_g, max_g + 1):
                out[r][c] = 2
            for d in (1, 2):
                if min_g - d >= 0:
                    out[r][min_g - d] = 1
                if max_g + d < W:
                    out[r][max_g + d] = 1
    for r in range(bands[-1][1] + 1, H):
        if all(grid[r][c] == 0 for c in range(W)):
            for c in stripe_cols:
                out[r][c] = 1
    return out