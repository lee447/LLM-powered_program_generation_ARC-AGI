def solve(grid):
    counts = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            c = grid[i][j]
            if c:
                counts[c] = counts.get(c, 0) + 1
    ringColors = sorted(counts, key=lambda c: counts[c], reverse=True)
    M = len(ringColors)
    S = counts[ringColors[0]]
    out = [[0] * S for _ in range(S)]
    for k, c in enumerate(ringColors):
        if k < M - 1:
            i0, i1 = k, S - 1 - k
            j0, j1 = k, S - 1 - k
            for j in range(j0, j1 + 1):
                out[i0][j] = c
                out[i1][j] = c
            for i in range(i0, i1 + 1):
                out[i][j0] = c
                out[i][j1] = c
        else:
            size = S - 2 * k
            if size == 1:
                m = S // 2
                out[m][m] = c
            else:
                i0, i1 = k, S - 1 - k
                j0, j1 = k, S - 1 - k
                for i in (i0, i1):
                    for j in (j0, j1):
                        out[i][j] = c
    return out