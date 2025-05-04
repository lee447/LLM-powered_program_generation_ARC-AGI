def solve(grid):
    H, W = len(grid), len(grid[0])
    zero_rows = {r for r in range(H) for c in range(W) if grid[r][c] == 0}
    zero_cols = {c for r in range(H) for c in range(W) if grid[r][c] == 0}
    if not zero_rows or not zero_cols:
        return grid
    min_r, max_r = min(zero_rows), max(zero_rows)
    min_c, max_c = min(zero_cols), max(zero_cols)
    h, w = max_r - min_r + 1, max_c - min_c + 1
    counts = {}
    for r in range(0, H - h + 1):
        for c in range(0, W - w + 1):
            if any(grid[r+i][c+j] == 0 for i in range(h) for j in range(w)):
                continue
            if not (r + h - 1 < min_r or r > max_r):
                continue
            block = tuple(tuple(grid[r+i][c:c+w]) for i in range(h))
            counts[block] = counts.get(block, 0) + 1
    if not counts:
        for r in range(0, H - h + 1):
            for c in range(0, W - w + 1):
                if any(grid[r+i][c+j] == 0 for i in range(h) for j in range(w)):
                    continue
                block = tuple(tuple(grid[r+i][c:c+w]) for i in range(h))
                counts[block] = counts.get(block, 0) + 1
    best = max(counts.items(), key=lambda x: x[1])[0]
    return [list(row) for row in best]