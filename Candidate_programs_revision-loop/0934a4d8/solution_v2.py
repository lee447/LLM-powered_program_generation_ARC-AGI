def solve(grid):
    H = len(grid)
    W = len(grid[0])
    minr, maxr, minc, maxc = H, -1, W, -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 8:
                if i < minr: minr = i
                if i > maxr: maxr = i
                if j < minc: minc = j
                if j > maxc: maxc = j
    if maxr < 0:
        return []
    h = maxr - minr + 1
    w = maxc - minc + 1
    counts = {}
    for i in range(H - h + 1):
        for j in range(W - w + 1):
            good = True
            rows = []
            for di in range(h):
                row = grid[i + di][j:j + w]
                for v in row:
                    if v == 8:
                        good = False
                        break
                if not good:
                    break
                rows.append(tuple(row))
            if not good:
                continue
            key = tuple(rows)
            counts[key] = counts.get(key, 0) + 1
    best = None
    bestc = -1
    for k, c in counts.items():
        if c > bestc:
            bestc = c
            best = k
    return [list(row) for row in best]