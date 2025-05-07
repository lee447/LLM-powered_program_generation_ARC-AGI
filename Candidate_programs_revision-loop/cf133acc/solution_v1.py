def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    Hs = [i for i in range(h) if sum(1 for x in grid[i] if x) >= 3]
    for H in sorted(Hs):
        row = grid[H]
        cols_by_color = {}
        for j, v in enumerate(row):
            if v:
                cols_by_color.setdefault(v, []).append(j)
        for c, js in cols_by_color.items():
            c1, c2 = min(js), max(js)
            pivot = None
            for j in range(c1, c2 + 1):
                if grid[H][j] == 0:
                    pivot = j
                    break
            if pivot is None:
                continue
            for j in range(c1, c2 + 1):
                out[H][j] = c
            for i in range(H):
                if out[i][pivot] == 0:
                    out[i][pivot] = c
    return out