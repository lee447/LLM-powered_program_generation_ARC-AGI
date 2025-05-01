def solve(grid):
    H, W = len(grid), len(grid[0])
    out = [[0]*W for _ in range(H)]
    shifts = [-1, 0, 1, 0]
    for c in {v for row in grid for v in row if v}:
        coords = [(r, x) for r in range(H) for x, v in enumerate(grid[r]) if v == c]
        rs = [r for r, _ in coords]
        cs = [x for _, x in coords]
        r0, r1 = min(rs), max(rs)
        stripe_rows = [r for r in range(r0, r1+1) if all(grid[r][x] == c for x in range(min(cs), max(cs)+1))]
        bar_cols = [x for x in range(min(cs), max(cs)+1) if any(grid[r][x] == c for r in range(r0, r1+1) if r not in stripe_rows)]
        base = stripe_rows[0]
        for r in range(r0, r1+1):
            shift = shifts[(r - base + 3) % 4]
            if r in stripe_rows:
                for x in range(min(cs), max(cs)+1):
                    if grid[r][x] == c:
                        nx = x + shift
                        if 0 <= nx < W:
                            out[r][nx] = c
            else:
                for x in bar_cols:
                    nx = x + shift
                    if 0 <= nx < W:
                        out[r][nx] = c
    return out