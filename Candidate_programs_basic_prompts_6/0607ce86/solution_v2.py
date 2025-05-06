def solve(grid):
    h = len(grid)
    w = len(grid[0])
    result = [[0]*w for _ in range(h)]
    cluster_info = {}
    block_rows = []
    for i, row in enumerate(grid):
        pos = [j for j, v in enumerate(row) if v != 0]
        clusters = []
        cur = []
        for j in pos:
            if not cur or j == cur[-1] + 1:
                cur.append(j)
            else:
                clusters.append(cur)
                cur = [j]
        if cur:
            clusters.append(cur)
        cl = [c for c in clusters if len(c) >= 2]
        if cl:
            cluster_info[i] = cl
            block_rows.append(i)
    block_groups = []
    prev = None
    for i in block_rows:
        if prev is None or i != prev + 1:
            block_groups.append([i])
        else:
            block_groups[-1].append(i)
        prev = i
    if not block_groups:
        return result
    first_group = block_groups[0]
    GH = len(first_group)
    patterns = []
    for r in first_group:
        cl = cluster_info[r]
        L = min(len(c) for c in cl)
        patt = []
        for k in range(L):
            counts = {}
            for c in cl:
                j = c[0] + k
                if j < w:
                    v = grid[r][j]
                    if v:
                        counts[v] = counts.get(v, 0) + 1
            best = 0
            maxc = -1
            for v, cnt in counts.items():
                if cnt > maxc or (cnt == maxc and v > best):
                    maxc = cnt
                    best = v
            patt.append(best)
        patterns.append(patt)
    for group in block_groups:
        if len(group) != GH:
            continue
        for idx, r in enumerate(group):
            patt = patterns[idx]
            L = len(patt)
            for c in cluster_info[r]:
                st = c[0]
                for k, v in enumerate(patt):
                    j = st + k
                    if 0 <= j < w:
                        result[r][j] = v
    return result