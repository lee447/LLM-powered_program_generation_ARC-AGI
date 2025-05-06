def solve(grid):
    f = len({c for row in grid for c in row})
    out = []
    for row in grid:
        new_row = row * f
        for _ in range(f):
            out.append(new_row)
    return out