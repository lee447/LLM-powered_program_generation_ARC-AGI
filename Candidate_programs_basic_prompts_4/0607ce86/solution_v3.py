def solve(grid):
    m, n = len(grid), len(grid[0])
    runs_by_j = {}
    for i in range(m):
        j = 0
        while j < n:
            if grid[i][j] != 0:
                j0 = j
                vals = []
                while j < n and grid[i][j] != 0:
                    vals.append(grid[i][j])
                    j += 1
                runs_by_j.setdefault(j0, []).append((i, vals))
            else:
                j += 1
    res = [[0] * n for _ in range(m)]
    for j0, runs in runs_by_j.items():
        if len(runs) < 2:
            continue
        run_map = {r: vals for r, vals in runs}
        rows = sorted(run_map)
        clusters = []
        start = prev = rows[0]
        for r in rows[1:]:
            if r == prev + 1:
                prev = r
            else:
                clusters.append((start, prev))
                start = prev = r
        clusters.append((start, prev))
        byH = {}
        for s, e in clusters:
            H = e - s + 1
            byH.setdefault(H, []).append(s)
        for H, starts in byH.items():
            if len(starts) < 2 or H < 1:
                continue
            widths = []
            for s in starts:
                for k in range(H):
                    widths.append(len(run_map[s + k]))
            # mode of widths
            cntw = {}
            for w in widths:
                cntw[w] = cntw.get(w, 0) + 1
            W = max(cntw, key=lambda x: cntw[x])
            template = [[0] * W for _ in range(H)]
            for k in range(H):
                for c in range(W):
                    cnt = {}
                    for s in starts:
                        v = run_map[s + k][c]
                        cnt[v] = cnt.get(v, 0) + 1
                    template[k][c] = max(cnt, key=lambda x: cnt[x])
            for s in starts:
                for k in range(H):
                    for c in range(W):
                        res[s + k][j0 + c] = template[k][c]
    return res