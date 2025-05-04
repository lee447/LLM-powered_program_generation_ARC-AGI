from collections import Counter

def solve(grid):
    rows, cols = len(grid), len(grid[0])
    stripe = next(j for j in range(cols) if any(grid[i][j] == 4 for i in range(rows)))
    left_cols = list(range(stripe))
    right_cols = list(range(stripe + 1, cols))
    left_vals = [grid[i][j] for i in range(rows) for j in left_cols if grid[i][j] != 0]
    right_vals = [grid[i][j] for i in range(rows) for j in right_cols if grid[i][j] != 0]
    target_left = Counter(left_vals).most_common(1)[0][0]
    target_right = Counter(right_vals).most_common(1)[0][0]
    lb = len(left_cols) // 2
    rb = len(right_cols) // 2
    bands = [
        (0, lb, target_left),
        (lb, stripe, target_left),
        (stripe + 1, stripe + 1 + rb, target_right),
        (stripe + 1 + rb, cols, target_right),
    ]
    out = []
    for i in range(rows):
        row = []
        for a, b, target in bands:
            v = 2 if any(grid[i][j] == target for j in range(a, b)) else 0
            row.append(v)
        out.append(row)
    return out