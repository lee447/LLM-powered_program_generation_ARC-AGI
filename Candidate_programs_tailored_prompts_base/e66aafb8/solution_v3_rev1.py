def solve(grid):
    R, C = len(grid), len(grid[0])
    r0, r1, c0, c1 = R, -1, C, -1
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                r0 = min(r0, i); r1 = max(r1, i)
                c0 = min(c0, j); c1 = max(c1, j)
    h, w = r1 - r0 + 1, c1 - c0 + 1
    cand_pos = []
    if r0 - h >= 0: cand_pos.append((r0 - h, c0))
    if r1 + 1 + h <= R: cand_pos.append((r1 + 1, c0))
    if c0 - w >= 0: cand_pos.append((r0, c0 - w))
    if c1 + 1 + w <= C: cand_pos.append((r0, c1 + 1))
    cands = []
    for si, sj in cand_pos:
        ok = True
        for i in range(h):
            for j in range(w):
                if grid[si + i][sj + j] == 0:
                    ok = False; break
            if not ok: break
        if ok:
            sub = [row[sj:sj + w] for row in grid[si:si + h]]
            cands.append(sub)
    def flips(sub):
        v = list(reversed(sub))
        hflip = [list(reversed(r)) for r in sub]
        vh = [list(reversed(r)) for r in reversed(sub)]
        return [sub, v, hflip, vh]
    best = None
    best_score = -1
    axes = (r0 + r1, c0 + c1)
    for sub in cands:
        for t in flips(sub):
            f = [list(row) for row in grid]
            for i in range(h):
                for j in range(w):
                    f[r0 + i][c0 + j] = t[i][j]
            score = 0
            ar, ac = axes
            for i in range(R):
                for j in range(C):
                    i2, j2 = ar - i, ac - j
                    if 0 <= i2 < R and 0 <= j2 < C and f[i][j] == f[i2][j2]:
                        score += 1
            if score > best_score:
                best_score = score
                best = t
    return best