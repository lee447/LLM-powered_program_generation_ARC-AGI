def solve(grid):
    R = len(grid)
    C = len(grid[0])
    pattern_color = 8
    coords = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == pattern_color]
    min_r = min(r for r, c in coords)
    min_c = min(c for r, c in coords)
    P0 = {(r - min_r, c - min_c) for r, c in coords}
    H0 = max(r for r, c in P0) + 1
    W0 = max(c for r, c in P0) + 1
    patterns = [(P0, H0, W0)]
    for _ in range(3):
        P_prev, H_prev, W_prev = patterns[-1]
        P_new = {(c, H_prev - 1 - r) for r, c in P_prev}
        patterns.append((P_new, W_prev, H_prev))
    matches = []
    for P, H, W in patterns:
        for i in range(R - H + 1):
            for j in range(C - W + 1):
                first = True
                v0 = None
                ok = True
                for dr, dc in P:
                    v = grid[i + dr][j + dc]
                    if first:
                        first = False
                        v0 = v
                        if v0 == 0 or v0 == pattern_color:
                            ok = False
                            break
                    else:
                        if v != v0:
                            ok = False
                            break
                if ok:
                    matches.append((i, j, P))
    out = [row[:] for row in grid]
    for i, j, P in matches:
        for dr, dc in P:
            out[i + dr][j + dc] = pattern_color
    return out