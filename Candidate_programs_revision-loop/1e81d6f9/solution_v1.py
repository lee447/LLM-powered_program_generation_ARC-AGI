def solve(grid):
    h, w = len(grid), len(grid[0])
    barcol = next(c for c in range(w) if all(r < h and grid[r][c] == 5 for r in range(4)))
    right = [(r, c, grid[r][c]) for r in range(h) for c in range(barcol+1, w) if grid[r][c] != 0]
    cnt = {}
    for r,c,v in right:
        cnt[v] = cnt.get(v, 0) + 1
    # pick the color whose right‐side occurrences are closest together vertically
    best, best_score = None, 1e9
    for v, f in cnt.items():
        ys = [r for r,c,u in right if u == v]
        score = max(ys) - min(ys) if ys else 1e9
        if score < best_score or (score == best_score and v < best):
            best, best_score = v, score
    rem = best
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(barcol+1, w):
            if out[r][c] == rem:
                out[r][c] = 0
    return out