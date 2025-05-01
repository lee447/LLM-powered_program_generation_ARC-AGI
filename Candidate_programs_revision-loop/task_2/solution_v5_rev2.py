def solve(grid):
    R, C = len(grid), len(grid[0])
    coords = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 8]
    if not coords:
        return grid
    r0, r1 = min(r for r, c in coords), max(r for r, c in coords)
    c0, c1 = min(c for r, c in coords), max(c for r, c in coords)
    H, W = r1 - r0 + 1, c1 - c0 + 1
    r_off, c_off = r0 % H, c0 % W
    patterns = {}
    for i in range(r_off, R - H + 1, H):
        for j in range(c_off, C - W + 1, W):
            block = []
            ok = True
            for di in range(H):
                row = grid[i + di][j:j + W]
                if 8 in row:
                    ok = False
                    break
                block.append(tuple(row))
            if ok:
                key = tuple(block)
                patterns[key] = patterns.get(key, 0) + 1
    best = max(patterns, key=patterns.get)
    return [list(r) for r in best]