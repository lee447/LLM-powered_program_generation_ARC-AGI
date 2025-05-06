def solve(grid: list[list[int]]) -> list[list[int]]:
    R, C = len(grid), len(grid[0])
    stripe_cols = [c for c in range(C) if all(grid[r][c] == grid[0][c] for r in range(R))]
    nonstripe_cols = [c for c in range(C) if c not in stripe_cols]
    bg_colors = [grid[r][nonstripe_cols[0]] for r in range(R)]
    row_reps = [r for r in range(R) if r == 0 or bg_colors[r] != bg_colors[r-1]]
    col_reps = []
    prev = -1
    for s in sorted(stripe_cols):
        if prev + 1 <= s - 1:
            col_reps.append(prev + 1)
        col_reps.append(s)
        prev = s
    if prev + 1 <= C - 1:
        col_reps.append(prev + 1)
    return [[grid[r][c] for c in col_reps] for r in row_reps]