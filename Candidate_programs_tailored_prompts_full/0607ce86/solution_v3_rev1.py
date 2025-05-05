def solve(grid):
    H = len(grid)
    W = len(grid[0]) if H else 0
    length_counts = {}
    for r in range(H):
        c = 0
        while c < W:
            if grid[r][c] != 0:
                start = c
                c += 1
                while c < W and grid[r][c] != 0:
                    c += 1
                l = c - start
                if l > 1:
                    length_counts[l] = length_counts.get(l, 0) + 1
            else:
                c += 1
    if not length_counts:
        return [[0] * W for _ in range(H)]
    stripeWidth = max(length_counts, key=lambda k: length_counts[k])
    runs = {}
    starts_set = set()
    for r in range(H):
        c = 0
        while c < W:
            if grid[r][c] != 0 and (c == 0 or grid[r][c - 1] == 0):
                end = c
                while end < W and grid[r][end] != 0:
                    end += 1
                L = end - c
                if L >= stripeWidth:
                    p = []
                    valid = True
                    for j in range(stripeWidth):
                        if grid[r][c + j] == 0:
                            valid = False
                            break
                        p.append(grid[r][c + j])
                    if valid:
                        runs[(r, c)] = tuple(p)
                        starts_set.add(c)
                c = end
            else:
                c += 1
    starts = sorted(starts_set)
    patterns_per_s = {s: [] for s in starts}
    for (r, s), p in runs.items():
        patterns_per_s[s].append(p)
    multiTpl = {}
    barTpl = {}
    for s, patterns in patterns_per_s.items():
        if not patterns:
            continue
        cnt = {}
        for p in patterns:
            cnt[p] = cnt.get(p, 0) + 1
        items = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        primary = items[0][0]
        multiTpl[s] = list(primary)
        if len(items) > 1:
            barTpl[s] = list(items[1][0])
    stripeRows = set(r for (r, s) in runs.keys())
    out = [[0] * W for _ in range(H)]
    for r in stripeRows:
        for s in starts:
            m = multiTpl[s]
            if (r, s) in runs:
                p = runs[(r, s)]
                dm = sum(1 for j, v in enumerate(p) if v != m[j])
                if s in barTpl:
                    b = barTpl[s]
                    db = sum(1 for j, v in enumerate(p) if v != b[j])
                    chosen = b if db < dm else m
                else:
                    chosen = m
            else:
                chosen = m
            for j in range(stripeWidth):
                out[r][s + j] = chosen[j]
    return out