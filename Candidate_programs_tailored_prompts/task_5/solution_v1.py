def solve(grid):
    h, w = len(grid), len(grid[0])
    refs = {1: [], 7: [], 9: []}
    pinks = []
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v == 6:
                pinks.append((i, j))
            elif v in refs:
                refs[v].append((i, j))
    out = [row[:] for row in grid]
    for i, j in pinks:
        best_col = None
        best_d = h + w
        for col, positions in refs.items():
            for x, y in positions:
                d = abs(x - i) + abs(y - j)
                if d < best_d:
                    best_d = d
                    best_col = col
        out[i][j] = best_col
    return out