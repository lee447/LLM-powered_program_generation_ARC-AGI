def solve(grid):
    H, W = len(grid), len(grid[0])
    y0, y1 = H, -1
    x0, x1 = W, -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 7:
                y0 = min(y0, i)
                y1 = max(y1, i)
                x0 = min(x0, j)
                x1 = max(x1, j)
    th, tw = y1 - y0 + 1, x1 - x0 + 1
    freq = {}
    for i in range(max(0, y0-2), min(H, y1+3)):
        for j in range(max(0, x0-2), min(W, x1+3)):
            if y0 <= i <= y1 and x0 <= j <= x1:
                continue
            if ((abs(i-y0) <= 2 or abs(i-y1) <= 2) and x0-2 <= j <= x1+2) or \
               ((abs(j-x0) <= 2 or abs(j-x1) <= 2) and y0-2 <= i <= y1+2):
                v = grid[i][j]
                if v != 7:
                    freq[v] = freq.get(v, 0) + 1
    filler = max(freq, key=freq.get) if freq else 6
    best = None
    bestf = None
    for i in range(H - th + 1):
        for j in range(W - tw + 1):
            cf = 0
            ok = True
            for di in range(th):
                for dj in range(tw):
                    v = grid[i+di][j+dj]
                    if v == 7:
                        ok = False
                        break
                    if v == filler:
                        cf += 1
                if not ok:
                    break
            if not ok:
                continue
            if best is None or cf < bestf:
                bestf = cf
                best = (i, j)
    bi, bj = best
    return [row[bj:bj+tw] for row in grid[bi:bi+th]]