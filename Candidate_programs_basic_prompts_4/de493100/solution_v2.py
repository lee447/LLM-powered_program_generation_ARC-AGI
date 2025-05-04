def solve(grid):
    h, w = len(grid), len(grid[0])
    min_r, max_r, min_c, max_c = h, -1, w, -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 7:
                if i < min_r: min_r = i
                if i > max_r: max_r = i
                if j < min_c: min_c = j
                if j > max_c: max_c = j
    H = max_r - min_r + 1
    W = max_c - min_c + 1
    def extract(r0, c0):
        return [row[c0:c0+W] for row in grid[r0:r0+H]]
    candidates = []
    if min_r - H >= 0: candidates.append(extract(min_r - H, min_c))
    if max_r + 1 + H <= h: candidates.append(extract(max_r + 1, min_c))
    if min_c - W >= 0: candidates.append(extract(min_r, min_c - W))
    if max_c + 1 + W <= w: candidates.append(extract(min_r, max_c + 1))
    for cand in candidates:
        ok = True
        for row in cand:
            for v in row:
                if v == 7:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return cand
    return []