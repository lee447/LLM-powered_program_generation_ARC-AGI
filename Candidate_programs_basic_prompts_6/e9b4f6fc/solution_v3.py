def solve(grid):
    H, W = len(grid), len(grid[0])
    def find_frame():
        best = None
        for r1 in range(H):
            for c1 in range(W):
                if grid[r1][c1] == 0: continue
                for r2 in range(r1+2, H):
                    for c2 in range(c1+2, W):
                        c = grid[r1][c1]
                        ok = True
                        for cc in range(c1, c2+1):
                            if grid[r1][cc] != c or grid[r2][cc] != c: ok = False; break
                        if not ok: continue
                        for rr in range(r1, r2+1):
                            if grid[rr][c1] != c or grid[rr][c2] != c: ok = False; break
                        if not ok: continue
                        area = (r2-r1+1)*(c2-c1+1)
                        if best is None or area > best[0]:
                            best = (area, r1, c1, r2, c2, c)
        return best
    bf = find_frame()
    if bf:
        _, r1, c1, r2, c2, frameColor = bf
        hasFrame = True
    else:
        r1 = H; c1 = W; r2 = -1; c2 = -1
        for i in range(H):
            for j in range(W):
                if grid[i][j] != 0:
                    r1 = min(r1, i); c1 = min(c1, j)
                    r2 = max(r2, i); c2 = max(c2, j)
        frameColor = None
        hasFrame = False
    clusters = []
    for i in range(H):
        for j in range(W):
            if hasFrame and r1 <= i <= r2 and c1 <= j <= c2: continue
        row = grid[i]
        j = 0
        while j < W:
            if (not hasFrame or i < r1 or i > r2) and ((j < c1 or j > c2) if hasFrame else True):
                if row[j] != 0:
                    k = j
                    vals = []
                    while k < W and row[k] != 0:
                        vals.append(row[k])
                        k += 1
                    if len(vals) == 2:
                        clusters.append(vals[0])
                    j = k
                    continue
            j += 1
    C = len(clusters)
    if hasFrame and C == 2:
        clusters_sorted = sorted(clusters)
    else:
        clusters_sorted = sorted(clusters, reverse=True)
    cropH, cropW = r2 - r1 + 1, c2 - c1 + 1
    inside_vals = set()
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if hasFrame and (i == r1 or i == r2 or j == c1 or j == c2): continue
            v = grid[i][j]
            if hasFrame and v == frameColor: continue
            inside_vals.add(v)
    inside_desc = sorted(inside_vals, reverse=True)
    mapping = {}
    for i, v in enumerate(inside_desc):
        if i < len(clusters_sorted):
            mapping[v] = clusters_sorted[i]
        else:
            mapping[v] = v
    out = [[0]*cropW for _ in range(cropH)]
    for i in range(cropH):
        for j in range(cropW):
            gi, gj = r1 + i, c1 + j
            v = grid[gi][gj]
            if hasFrame and (i == 0 or i == cropH-1 or j == 0 or j == cropW-1):
                out[i][j] = v
            else:
                if hasFrame and v == frameColor:
                    out[i][j] = v
                else:
                    out[i][j] = mapping.get(v, v)
    return out