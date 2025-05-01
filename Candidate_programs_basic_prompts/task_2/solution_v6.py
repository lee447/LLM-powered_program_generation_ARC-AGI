def solve(grid):
    n, m = len(grid), len(grid[0])
    freq = {}
    for i in range(n):
        for j in range(m):
            v = grid[i][j]
            if v != 0:
                freq[v] = freq.get(v, 0) + 1
    mask_color = min(freq, key=lambda k: freq[k])
    coords = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == mask_color]
    min_r = min(i for i, j in coords)
    max_r = max(i for i, j in coords)
    min_c = min(j for i, j in coords)
    max_c = max(j for i, j in coords)
    h = max_r - min_r + 1
    w = max_c - min_c + 1
    pattern_counts = {}
    for si in range(n - h + 1):
        for sj in range(m - w + 1):
            ok = True
            for ii in range(si, si + h):
                for jj in range(sj, sj + w):
                    if grid[ii][jj] == mask_color:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            pat = tuple(tuple(grid[ii][jj] for jj in range(sj, sj + w)) for ii in range(si, si + h))
            pattern_counts[pat] = pattern_counts.get(pat, 0) + 1
    best = max(pattern_counts, key=lambda p: pattern_counts[p])
    return [list(row) for row in best]