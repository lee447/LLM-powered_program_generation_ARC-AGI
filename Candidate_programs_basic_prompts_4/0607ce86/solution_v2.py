def solve(grid):
    H = len(grid)
    W = len(grid[0])
    row_counts = [sum(1 for v in row if v != 0) for row in grid]
    Trow = (max(row_counts) + 1) // 2
    masked = [row[:] for row in grid]
    for i in range(H):
        if row_counts[i] < Trow:
            for j in range(W):
                masked[i][j] = 0
    col_counts = [sum(1 for i in range(H) if masked[i][j] != 0) for j in range(W)]
    Tcol = (max(col_counts) + 1) // 2
    for j in range(W):
        if col_counts[j] < Tcol:
            for i in range(H):
                masked[i][j] = 0
    for i in range(H):
        if row_counts[i] < Trow:
            continue
        segs = []
        j = 0
        while j < W:
            if masked[i][j] != 0:
                start = j
                while j < W and masked[i][j] != 0:
                    j += 1
                segs.append((start, j - 1))
            else:
                j += 1
        if len(segs) <= 1:
            continue
        best = None
        best_score = -1
        for (s, e) in segs:
            cnt = {}
            for k in range(s, e + 1):
                cnt[masked[i][k]] = cnt.get(masked[i][k], 0) + 1
            mc = max(cnt.values())
            if mc > best_score:
                best_score = mc
                best = (s, e)
        ts, te = best
        L = te - ts + 1
        template = [masked[i][k] for k in range(ts, te + 1)]
        for (s, e) in segs:
            if e - s + 1 != L or (s == ts and e == te):
                continue
            for d in range(L):
                masked[i][s + d] = template[d]
    return masked