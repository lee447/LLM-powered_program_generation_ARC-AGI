def solve(grid):
    H = len(grid)
    W = len(grid[0])
    h_seps = []
    for i in range(H):
        row = grid[i]
        cnt = {}
        for v in row:
            cnt[v] = cnt.get(v, 0) + 1
        if len(cnt) <= 2 and max(cnt.values()) * 2 > W:
            h_seps.append(i)
    h_barcount = len(h_seps)
    v_seps = []
    for j in range(W):
        col = [grid[i][j] for i in range(H)]
        uniq = set(col)
        if len(uniq) <= 3:
            cnt = {}
            for v in col:
                cnt[v] = cnt.get(v, 0) + 1
            mc = max(cnt.values())
            trans = 0
            for i in range(H - 1):
                if col[i] != col[i + 1]:
                    trans += 1
            if mc * 2 > H and trans <= 2 * h_barcount:
                v_seps.append(j)
    v_seps.sort()
    segs = []
    p = 0
    for s in v_seps:
        if p <= s - 1:
            segs.append((p, s - 1))
        p = s + 1
    if p <= W - 1:
        segs.append((p, W - 1))
    rep_j = [start for start, end in segs if start <= end]
    out_cols = []
    sv = set(v_seps)
    sr = set(rep_j)
    for j in range(W):
        if j in sv or j in sr:
            out_cols.append(j)
    rep_rows = []
    prev = None
    c0 = rep_j[0]
    for i in range(H):
        v = grid[i][c0]
        if i == 0 or v != prev:
            rep_rows.append(i)
        prev = v
    return [[grid[i][j] for j in out_cols] for i in rep_rows]