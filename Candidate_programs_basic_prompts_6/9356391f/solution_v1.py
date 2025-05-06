def solve(grid):
    h, w = len(grid), len(grid[0])
    row0 = grid[0]
    nonzeros = [j for j, v in enumerate(row0) if v != 0]
    minc, maxc = min(nonzeros), max(nonzeros)
    shape = row0[minc:maxc+1]
    layers = len(shape) - 1
    seed_r = seed_c = None
    for i in range(2, h):
        for j in range(w):
            if grid[i][j] != 0:
                seed_r, seed_c = i, j
                break
        if seed_r is not None:
            break
    out = [list(r) for r in grid]
    for i in range(max(0, seed_r-layers), min(h, seed_r+layers+1)):
        for j in range(max(0, seed_c-layers), min(w, seed_c+layers+1)):
            d = max(abs(i-seed_r), abs(j-seed_c))
            if d <= layers:
                out[i][j] = shape[d]
    return out