def solve(grid):
    h0 = len(grid)
    w0 = len(grid[0])
    min_r, max_r = h0, -1
    min_c, max_c = w0, -1
    for i in range(h0):
        for j in range(w0):
            if grid[i][j] == 8:
                if i < min_r: min_r = i
                if i > max_r: max_r = i
                if j < min_c: min_c = j
                if j > max_c: max_c = j
    bh = max_r - min_r + 1
    bw = max_c - min_c + 1
    from collections import Counter
    cnt = Counter()
    locs = {}
    for i in range(h0 - bh + 1):
        for j in range(w0 - bw + 1):
            if i <= min_r <= i+bh-1 and j <= min_c <= j+bw-1:
                continue
            ok = True
            key = []
            for di in range(bh):
                row = grid[i+di][j:j+bw]
                if 8 in row:
                    ok = False
                    break
                key.append(tuple(row))
            if not ok:
                continue
            key = tuple(key)
            cnt[key] += 1
            locs[key] = (i, j)
    best = cnt.most_common(1)[0][0]
    out = [list(row) for row in best]
    return out