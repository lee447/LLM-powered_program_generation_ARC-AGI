def solve(grid):
    h, w = len(grid), len(grid[0])
    col_nz = [sum(1 for r in range(h) if grid[r][c] != 0) for c in range(w)]
    cuts = [i for i, v in enumerate(col_nz) if v == 0]
    segs = []
    cur = []
    for c in range(w):
        if c in cuts:
            if cur:
                segs.append(cur)
                cur = []
        else:
            cur.append(c)
    if cur:
        segs.append(cur)
    segs = sorted(segs, key=lambda s: s[0])
    if len(segs) > 3:
        segs = sorted(segs, key=lambda s: len(s), reverse=True)[:3]
        segs = sorted(segs, key=lambda s: s[0])
    reps = []
    for seg in segs:
        cnt = {}
        for r in range(h):
            for c in seg:
                v = grid[r][c]
                if v != 0:
                    cnt[v] = cnt.get(v, 0) + 1
        rep = max(cnt.items(), key=lambda x: x[1])[0] if cnt else 0
        reps.append(rep)
    if len(reps) < 3:
        reps += [0] * (3 - len(reps))
    out = [[0] * 3 for _ in range(3)]
    if reps[0] != reps[1] and reps[1] != reps[2] and reps[0] != reps[2]:
        for i in range(3):
            for j in range(3):
                out[i][j] = reps[i]
    else:
        if reps[1] == reps[2]:
            for i in (1, 2):
                for j in range(3):
                    out[i][j] = reps[1]
            out[0][0] = reps[0]
        elif reps[0] == reps[1]:
            for j in range(3):
                out[0][j] = reps[0]
            out[2][2] = reps[2]
        else:
            for i in range(3):
                out[i][0] = reps[0]
            out[0][1] = reps[1]
            out[1][1] = reps[1]
    return out