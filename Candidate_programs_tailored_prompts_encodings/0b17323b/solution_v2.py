def solve(grid):
    n, m = len(grid), len(grid[0])
    L = min(n, m)
    P = [i for i in range(L) if grid[i][i] == 1]
    candidates = []
    S = set(P)
    for p in P:
        for q in P:
            if q > p:
                d = q - p
                if p + 2 * d in S:
                    candidates.append((p, d))
    seqs = []
    used = set()
    for p, d in sorted(candidates):
        if d not in used:
            seqs.append((p, d))
            used.add(d)
    out = [row[:] for row in grid]
    for p, d in seqs:
        k = 0
        while p + (k + 1) * d in S:
            k += 1
        x = p + (k + 1) * d
        while x < L:
            out[x][x] = 2
            x += d
    return out