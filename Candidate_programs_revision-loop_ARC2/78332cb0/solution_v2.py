def solve(grid):
    n = len(grid)
    m = len(grid[0])
    seprows = [i for i in range(n) if all(grid[i][j] == 6 for j in range(m))]
    sepcols = [j for j in range(m) if all(grid[i][j] == 6 for i in range(n))]
    rs = []
    prev = 0
    for r in sorted(seprows):
        if prev < r:
            rs.append((prev, r))
        prev = r + 1
    if prev < n:
        rs.append((prev, n))
    cs = []
    prev = 0
    for c in sorted(sepcols):
        if prev < c:
            cs.append((prev, c))
        prev = c + 1
    if prev < m:
        cs.append((prev, m))
    R = len(rs)
    C = len(cs)
    blocks = []
    for i in range(R):
        r0, r1 = rs[i]
        rowblock = []
        for j in range(C):
            c0, c1 = cs[j]
            rowblock.append([row[c0:c1] for row in grid[r0:r1]])
        blocks.append(rowblock)
    if R > 1 and C == 1:
        seq = [blocks[i][0] for i in range(R - 1, -1, -1)]
        h = len(seq[0])
        out = []
        for i, b in enumerate(seq):
            for row in b:
                out.append(row[:])
            if i != len(seq) - 1:
                out.append([6] * len(b[0]))
        return out
    if R == 1 and C > 1:
        seq = [blocks[0][j] for j in range(C)]
        w = len(seq[0][0])
        h = len(seq[0])
        out = []
        for i in range(h):
            row = []
            for j, b in enumerate(seq):
                row.extend(b[i])
                if j != len(seq) - 1:
                    row.append(6)
            out.append(row)
        return out
    seq = []
    for d in range(max(R, C)):
        grp = [(i, j) for i in range(R) for j in range(C) if abs(i - j) == d]
        grp.sort()
        for i, j in grp:
            seq.append(blocks[i][j])
    h = len(seq[0])
    w = len(seq[0][0])
    out = []
    for i, b in enumerate(seq):
        for row in b:
            out.append(row[:])
        if i != len(seq) - 1:
            out.append([6] * w)
    return out