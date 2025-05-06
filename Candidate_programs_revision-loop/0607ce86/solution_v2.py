def solve(grid):
    H, W = len(grid), len(grid[0])
    def transpose(g):
        return [[g[i][j] for i in range(len(g))] for j in range(len(g[0]))]
    def find_period(length, data, width):
        best_p, best_score = 1, -1.0
        for p in range(1, length):
            match = 0
            total = 0
            for i in range(length - p):
                for j in range(width):
                    if data[i][j] == data[i + p][j]:
                        match += 1
                    total += 1
            ratio = match / total
            if ratio > best_score:
                best_score, best_p = ratio, p
        return best_p
    vt = grid
    hz = transpose(grid)
    vp = find_period(H, vt, W)
    hp = find_period(W, hz, H)
    pattern = [[0] * hp for _ in range(vp)]
    for i in range(vp):
        for j in range(hp):
            counts = {}
            for bi in range(i, H, vp):
                for bj in range(j, W, hp):
                    v = grid[bi][bj]
                    counts[v] = counts.get(v, 0) + 1
            mc = max(counts.items(), key=lambda x: x[1])[0]
            pattern[i][j] = mc
    res = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            res[i][j] = pattern[i % vp][j % hp]
    return res