def solve(grid):
    h = len(grid)
    w = len(grid[0])
    # find a pattern row (contains values >1)
    for i in range(h):
        if any(cell > 1 for cell in grid[i]):
            pattern_row = grid[i]
            break
    # extract non-zero elements from the pattern row
    pr = [v for v in pattern_row if v != 0]
    # find minimal period
    for p in range(1, len(pr) + 1):
        if len(pr) % p == 0 and pr == pr[:p] * (len(pr) // p):
            cycle = pr[:p]
            break
    out = []
    for row in grid:
        if any(cell > 1 for cell in row):
            r = [cycle[j % len(cycle)] for j in range(w)]
        else:
            r = [1] * w
        out.append(r)
    return out