def solve(grid):
    H, W = len(grid), len(grid[0])
    zero_rows = [r for r in range(H) for c in range(W) if grid[r][c] == 0]
    if not zero_rows:
        return grid
    zero_cols = [c for r in range(H) for c in range(W) if grid[r][c] == 0]
    min_r, max_r = min(zero_rows), max(zero_rows)
    min_c, max_c = min(zero_cols), max(zero_cols)
    h, w = max_r - min_r + 1, max_c - min_c + 1
    counts = {}
    for r in range(H - h + 1):
        for c in range(W - w + 1):
            ok = True
            block = []
            for i in range(h):
                row = grid[r + i][c:c + w]
                if 0 in row:
                    ok = False
                    break
                block.append(tuple(row))
            if not ok:
                continue
            key = tuple(block)
            counts[key] = counts.get(key, 0) + 1
    best = max(counts, key=counts.get)
    return [list(row) for row in best]