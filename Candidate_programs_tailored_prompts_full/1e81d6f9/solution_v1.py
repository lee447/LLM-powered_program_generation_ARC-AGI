def solve(grid):
    R, C = len(grid), len(grid[0])
    grey = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 5]
    if not grey:
        return grid
    min_r = min(r for r, c in grey)
    max_r = max(r for r, c in grey)
    min_c = min(c for r, c in grey)
    max_c = max(c for r, c in grey)
    hole_rs = range(min_r + 1, max_r)
    hole_cs = range(min_c + 1, max_c)
    target = None
    for r in hole_rs:
        for c in hole_cs:
            v = grid[r][c]
            if v != 0:
                target = v
                break
        if target is not None:
            break
    out = [row[:] for row in grid]
    if target is not None:
        for r in range(R):
            for c in range(C):
                if out[r][c] == target and not (r in hole_rs and c in hole_cs):
                    out[r][c] = 0
    return out