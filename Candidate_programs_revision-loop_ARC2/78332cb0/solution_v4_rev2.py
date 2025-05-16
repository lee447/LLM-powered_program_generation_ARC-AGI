def solve(grid):
    n = len(grid)
    m = len(grid[0])
    seprows = [i for i in range(n) if all(grid[i][j] == 6 for j in range(m))]
    sepcols = [j for j in range(m) if all(grid[i][j] == 6 for i in range(n))]
    rs = []
    prev = 0
    for i in sorted(seprows):
        if prev < i:
            rs.append((prev, i))
        prev = i + 1
    if prev < n:
        rs.append((prev, n))
    cs = []
    prev = 0
    for j in sorted(sepcols):
        if prev < j:
            cs.append((prev, j))
        prev = j + 1
    if prev < m:
        cs.append((prev, m))
    blocks = [[[row[c0:c1] for row in grid[r0:r1]] for c0, c1 in cs] for r0, r1 in rs]
    R = len(rs)
    C = len(cs)
    if R == 1 and C == 1:
        return grid
    H = len(blocks[0][0])
    W = len(blocks[0][0][0])
    out = []
    if R > 1 and C == 1:
        seq = [blocks[i][0] for i in range(R - 1, -1, -1)]
        for i in range(H):
            row = []
            for k, b in enumerate(seq):
                row += b[i]
                if k != len(seq) - 1:
                    row.append(6)
            out.append(row)
        return out
    if R == 1 and C > 1:
        seq = [blocks[0][j] for j in range(C)]
        for k, b in enumerate(seq):
            for r in b:
                out.append(r[:])
            if k != len(seq) - 1:
                out.append([6] * W)
        return out
    seq = []
    for k in range(min(R, C)):
        seq.append(blocks[k][k])
    for i in range(R):
        for j in range(C):
            if i < j:
                seq.append(blocks[i][j])
    for i in range(R):
        for j in range(C):
            if i > j:
                seq.append(blocks[i][j])
    for k, b in enumerate(seq):
        for r in b:
            out.append(r[:])
        if k != len(seq) - 1:
            out.append([6] * W)
    return out