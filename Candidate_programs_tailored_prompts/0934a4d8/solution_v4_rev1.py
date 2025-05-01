def solve(grid):
    h = len(grid)
    w = len(grid[0])
    min_r, min_c, max_r, max_c = h, w, -1, -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8:
                if i < min_r: min_r = i
                if i > max_r: max_r = i
                if j < min_c: min_c = j
                if j > max_c: max_c = j
    H = max_r - min_r + 1
    W = max_c - min_c + 1
    counts = {}
    for i in range(h - H + 1):
        for j in range(w - W + 1):
            ok = True
            for di in range(H):
                for dj in range(W):
                    if grid[i + di][j + dj] == 8:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            key = tuple(tuple(grid[i + di][j:j + W]) for di in range(H))
            counts[key] = counts.get(key, 0) + 1
    best = max(counts.items(), key=lambda x: x[1])[0]
    return [list(row) for row in best]