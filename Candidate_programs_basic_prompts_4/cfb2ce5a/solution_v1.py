def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import Counter
    cnt = Counter(v for row in grid for v in row if v != 0)
    cols = [c for c,_ in cnt.most_common(2)]
    cset = set(cols)
    r0 = h; r1 = -1; c0 = w; c1 = -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] in cset:
                r0 = min(r0, i); r1 = max(r1, i)
                c0 = min(c0, j); c1 = max(c1, j)
    H, W = r1 - r0 + 1, c1 - c0 + 1
    orig = [row[c0:c1+1] for row in grid[r0:r1+1]]
    def rot90(a):
        return [[a[H-1-j][i] for j in range(H)] for i in range(W)]
    def rot180(a):
        return [row[::-1] for row in a[::-1]]
    def rot270(a):
        return [[a[j][W-1-i] for j in range(H)] for i in range(W)]
    R90, R180, R270 = rot90(orig), rot180(orig), rot270(orig)
    out = [row[:] for row in grid]
    def fill(R, br, bc, markers):
        m = {}
        # gather remaps from any nonzero in input under this block
        for i in range(len(R)):
            for j in range(len(R[0])):
                v = grid[br+i][bc+j]
                if v != 0:
                    m[R[i][j]] = v
        vals = set(R[i][j] for i in range(len(R)) for j in range(len(R[0])))
        # if only one map, the other maps to 0
        if len(m) == 1:
            x = next(iter(vals - set(m)))
            m[x] = 0
        # apply
        for i in range(len(R)):
            for j in range(len(R[0])):
                out[br+i][bc+j] = m.get(R[i][j], 0)
    # NE
    fill(R90, r0, c1+1, None)
    # SW
    fill(R270, r1+1, c0, None)
    # SE
    fill(R180, r1+1, c1+1, None)
    return out