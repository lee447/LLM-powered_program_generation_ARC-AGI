def solve(grid):
    H, W = len(grid), len(grid[0])
    y0, y1 = H, -1
    x0, x1 = W, -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 7:
                if i < y0: y0 = i
                if i > y1: y1 = i
                if j < x0: x0 = j
                if j > x1: x1 = j
    th, tw = y1 - y0 + 1, x1 - x0 + 1
    best = None
    best6 = None
    for i in range(H - th + 1):
        for j in range(W - tw + 1):
            c6 = 0
            ok = True
            for di in range(th):
                for dj in range(tw):
                    v = grid[i+di][j+dj]
                    if v == 7:
                        ok = False
                        break
                    if v == 6:
                        c6 += 1
                if not ok:
                    break
            if not ok:
                continue
            if best is None or c6 < best6:
                best6 = c6
                best = (i, j)
                if c6 == 0:
                    break
        else:
            continue
        break
    bi, bj = best
    return [row[bj:bj+tw] for row in grid[bi:bi+th]]