def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_scores = {}
    for c in range(1, 10):
        sc = 0
        for i in range(h):
            if all(grid[i][j] == c for j in range(w)):
                sc += 1
        for j in range(w):
            if all(grid[i][j] == c for i in range(h)):
                sc += 1
        sep_scores[c] = sc
    sep = max(sep_scores, key=sep_scores.get)
    counts = {}
    for i in range(h - 1):
        for j in range(w - 1):
            c = grid[i][j]
            if c not in (0, sep):
                if grid[i][j + 1] == c and grid[i + 1][j] == c and grid[i + 1][j + 1] == c:
                    counts[c] = counts.get(c, 0) + 1
    items = sorted(counts.items(), key=lambda x: x[1])
    if not items:
        return []
    mx = max(cnt for _, cnt in items)
    out = []
    for c, cnt in items:
        out.append([c] * cnt + [0] * (mx - cnt))
    return out