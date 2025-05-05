def solve(grid):
    h, w = len(grid), len(grid[0])
    coords8 = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
    r1 = min(r for r, c in coords8)
    r2 = max(r for r, c in coords8)
    c1 = min(c for r, c in coords8)
    c2 = max(c for r, c in coords8)
    H, W = r2 - r1 + 1, c2 - c1 + 1
    counts = {}
    for i in range(h - H + 1):
        for j in range(w - W + 1):
            pat = []
            skip = False
            for di in range(H):
                row = grid[i + di][j:j + W]
                if 8 in row:
                    skip = True
                    break
                pat.append(tuple(row))
            if skip:
                continue
            pat = tuple(pat)
            counts[pat] = counts.get(pat, 0) + 1
    best = max(counts, key=lambda k: counts[k])
    return [list(row) for row in best]