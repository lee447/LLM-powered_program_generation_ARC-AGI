def solve(grid):
    N, M = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    grey_rows = [r for r in range(N) if any(grid[r][c] == 5 for c in range(M))]
    bands = []
    if grey_rows:
        start = prev = grey_rows[0]
        for r in grey_rows[1:]:
            if r == prev + 1:
                prev = r
            else:
                bands.append((start, prev))
                start = prev = r
        bands.append((start, prev))
    grey_cols = sorted({c for r in range(bands[0][0], bands[0][1]+1) for c in range(M) if grid[r][c] == 5})
    block_starts = [c for c in grey_cols if c+1 in grey_cols]
    min_col = block_starts[0]
    max_col = block_starts[-1] + 1
    # fill inside bands
    for start, end in bands:
        for r in range(start, end+1):
            for i in range(len(block_starts)-1):
                a = block_starts[i] + 2
                b = block_starts[i+1] - 1
                for c in range(a, b+1):
                    if out[r][c] != 5:
                        out[r][c] = 2
    # separator rows between bands
    for i in range(len(bands)-1):
        e = bands[i][1]
        s2 = bands[i+1][0]
        for r in range(e+1, s2):
            for c in range(min_col, max_col+1):
                out[r][c] = 2
            for c in range(0, min_col):
                out[r][c] = 1
            for c in range(max_col+1, M):
                out[r][c] = 1
    # bottom rows after last band
    last_end = bands[-1][1] if bands else -1
    if last_end < N-1:
        stripe_cols = []
        for i in range(len(block_starts)-1):
            a = block_starts[i] + 2
            b = block_starts[i+1] - 1
            stripe_cols.extend(range(a, b+1))
        for r in range(last_end+1, N):
            for c in stripe_cols:
                out[r][c] = 1
    return out