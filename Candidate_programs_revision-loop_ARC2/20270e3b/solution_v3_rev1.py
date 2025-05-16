def solve(grid):
    h, w = len(grid), len(grid[0])
    sep = None
    for c in range(w):
        v = grid[0][c]
        if v in (1, 7) and all(grid[r][c] == v for r in range(h)):
            sep = c
            break
    if sep is not None:
        g = [row[:sep] for row in grid]
        out = []
        for row in g:
            v = row[0]
            if not (v in (1, 7) and all(x == v for x in row)):
                out.append([4 if x == 7 else x for x in row])
        return out
    pure_rows = set(i for i, row in enumerate(grid) if row[0] in (1, 7) and all(x == row[0] for x in row))
    g = [[4 if x == 7 else x for x in row] for i, row in enumerate(grid) if i not in pure_rows]
    if len(g) == h and len(g[0]) == w:
        base = g[:h-2]
        block = [row[w-3:] for row in g][2:]
        return [base[i] + block[i] for i in range(h-2)]
    return g