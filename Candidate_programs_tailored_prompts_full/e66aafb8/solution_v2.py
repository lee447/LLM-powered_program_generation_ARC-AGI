def solve(grid):
    H, W = len(grid), len(grid[0])
    # find zero‐band columns
    zero_cols = sorted({c for r in range(H) for c in range(W) if grid[r][c] == 0})
    C0, C1 = zero_cols[0], zero_cols[-1]
    # keep only rows that contain at least one true color (not 0 or 8)
    good_rows = [r for r in range(H) if any(grid[r][c] not in (0, 8) for c in range(W))]
    # keep only columns that contain at least one true color
    good_cols = [c for c in range(W) if any(grid[r][c] not in (0, 8) for r in range(H))]
    # build subgrid without zeros‐band columns
    sub = []
    for r in good_rows:
        row = []
        for c in good_cols:
            if c < C0 or c > C1:
                row.append(grid[r][c])
        sub.append(row)
    # collapse each pair of identical rows
    half = [sub[i] for i in range(0, len(sub), 2)]
    # take stripe of width zero‐band immediately next to zeros
    stripe_start = sum(1 for c in good_cols if c < C0)
    stripe = [row[stripe_start:stripe_start + len(zero_cols)] for row in half]
    # flip vertically
    return stripe[::-1]