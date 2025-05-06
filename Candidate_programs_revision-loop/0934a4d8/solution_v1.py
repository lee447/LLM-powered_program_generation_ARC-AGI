def solve(grid):
    h, w = len(grid), len(grid[0])
    pts = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 8]
    if not pts:
        return []
    ys = [i for i, _ in pts]
    xs = [j for _, j in pts]
    y0, y1 = min(ys), max(ys)
    x0, x1 = min(xs), max(xs)
    H, W = y1 - y0 + 1, x1 - x0 + 1
    from collections import Counter
    cnt = Counter()
    for i in range(h - H + 1):
        for j in range(w - W + 1):
            ok = True
            block = []
            for di in range(H):
                row = grid[i+di][j:j+W]
                if 8 in row:
                    ok = False
                    break
                block.append(tuple(row))
            if ok:
                cnt[tuple(block)] += 1
    best = cnt.most_common(1)[0][0]
    return [list(row) for row in best]