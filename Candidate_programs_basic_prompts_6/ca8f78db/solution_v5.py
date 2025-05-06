def solve(grid):
    h, w = len(grid), len(grid[0])
    uniform = [False] * h
    for i, row in enumerate(grid):
        nz = [v for v in row if v != 0]
        if nz and len(set(nz)) == 1 or not nz:
            uniform[i] = True
    pattern_row_idx = None
    for i, row in enumerate(grid):
        if 0 not in row and not uniform[i]:
            pattern_row_idx = i
            break
    pattern = grid[pattern_row_idx]
    period = w
    for p in range(1, w + 1):
        if w % p: continue
        if all(pattern[j] == pattern[j % p] for j in range(w)):
            period = p
            break
    color_solid = [None] * h
    for i, row in enumerate(grid):
        nz = [v for v in row if v != 0]
        color_solid[i] = nz[0] if nz else 0
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if out[i][j] == 0:
                if uniform[i]:
                    out[i][j] = color_solid[i]
                else:
                    out[i][j] = pattern[j % period]
    return out