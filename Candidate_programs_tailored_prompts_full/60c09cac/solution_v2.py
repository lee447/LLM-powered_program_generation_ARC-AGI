def solve(grid):
    out = []
    for row in grid:
        scaled = []
        for v in row:
            scaled.extend([v, v])
        out.append(scaled)
        out.append(scaled[:])
    return out