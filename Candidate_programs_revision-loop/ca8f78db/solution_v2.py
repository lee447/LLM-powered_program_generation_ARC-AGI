def solve(grid):
    h, w = len(grid), len(grid[0])
    base_pattern = None
    for row in grid:
        non0 = set(row) - {0}
        if len(non0) > 1 and 0 not in row:
            base_pattern = row[:]
            break
    for r in range(h):
        row = grid[r]
        non0 = set(row) - {0}
        if len(non0) == 1:
            fill = next(iter(non0))
            for c in range(w):
                if row[c] == 0:
                    row[c] = fill
        elif len(non0) > 1:
            for c in range(w):
                if row[c] == 0:
                    row[c] = base_pattern[c]
    return grid