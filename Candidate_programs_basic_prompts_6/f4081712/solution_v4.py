def solve(grid):
    h0 = len(grid)
    w0 = len(grid[0])
    pos = {}
    for i in range(h0):
        for j in range(w0):
            pos.setdefault(grid[i][j], []).append((i, j))
    cand = []
    for c, ls in pos.items():
        r0 = min(i for i, _ in ls)
        r1 = max(i for i, _ in ls)
        c0 = min(j for _, j in ls)
        c1 = max(j for _, j in ls)
        area = (r1 - r0 + 1) * (c1 - c0 + 1)
        if len(ls) == area:
            cand.append((area, c, r0, r1, c0, c1))
    _, stripe_color, r0, r1, c0, c1 = max(cand)
    h = r1 - r0 + 1
    w = c1 - c0 + 1
    freq = {}
    for i in range(h0 - h + 1):
        for j in range(w0 - w + 1):
            ok = True
            block = []
            for di in range(h):
                row = grid[i + di][j:j + w]
                if stripe_color in row:
                    ok = False
                    break
                block.append(tuple(row))
            if ok:
                t = tuple(block)
                freq[t] = freq.get(t, 0) + 1
    best = max(freq, key=lambda k: freq[k])
    return [list(row) for row in best]