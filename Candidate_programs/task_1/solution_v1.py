def solve(grid):
    H = len(grid)
    W = len(grid[0])
    row_nz = [sum(1 for v in row if v != 0) for row in grid]
    thresh_row = W // 4
    row_mask = [c > thresh_row for c in row_nz]
    row_segs = []
    i = 0
    while i < H:
        if row_mask[i]:
            s = i
            while i < H and row_mask[i]:
                i += 1
            row_segs.append((s, i - s))
        else:
            i += 1
    counts = {}
    for _, l in row_segs:
        counts[l] = counts.get(l, 0) + 1
    B = max(counts, key=lambda x: counts[x])
    row_segs = [(s, l) for s, l in row_segs if l == B]
    col_nz = [sum(1 for r in range(H) if grid[r][c] != 0) for c in range(W)]
    thresh_col = H // 4
    col_mask = [c > thresh_col for c in col_nz]
    col_segs = []
    j = 0
    while j < W:
        if col_mask[j]:
            s = j
            while j < W and col_mask[j]:
                j += 1
            col_segs.append((s, j - s))
        else:
            j += 1
    counts = {}
    for _, l in col_segs:
        counts[l] = counts.get(l, 0) + 1
    C = max(counts, key=lambda x: counts[x])
    col_segs = [(s, l) for s, l in col_segs if l == C]
    pattern = [[0] * C for _ in range(B)]
    for dr in range(B):
        for dc in range(C):
            cnts = {}
            for rs, _ in row_segs:
                for cs, _ in col_segs:
                    v = grid[rs + dr][cs + dc]
                    cnts[v] = cnts.get(v, 0) + 1
            bestv = None
            bestc = -1
            for v, c in cnts.items():
                if c > bestc or (c == bestc and (bestv is None or v < bestv)):
                    bestv = v
                    bestc = c
            pattern[dr][dc] = bestv
    out = [[0] * W for _ in range(H)]
    for rs, _ in row_segs:
        for cs, _ in col_segs:
            for dr in range(B):
                for dc in range(C):
                    out[rs + dr][cs + dc] = pattern[dr][dc]
    return out