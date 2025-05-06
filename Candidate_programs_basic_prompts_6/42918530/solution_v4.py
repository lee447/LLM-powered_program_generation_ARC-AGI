def solve(grid):
    h, w = len(grid), len(grid[0])
    rows = [i for i in range(h) if all(grid[i][j] == 0 for j in range(w))]
    cols = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    br, bc = [], []
    for a, b in zip(rows, rows[1:]):
        if b - a > 1:
            br.append((a + 1, b))
    for a, b in zip(cols, cols[1:]):
        if b - a > 1:
            bc.append((a + 1, b))
    B, C = len(br), len(bc)
    blocks = [[None]*C for _ in range(B)]
    for i, (r0, r1) in enumerate(br):
        for j, (c0, c1) in enumerate(bc):
            sub = [row[c0:c1] for row in grid[r0:r1]]
            blocks[i][j] = sub
    def pat_plus(col):
        p = [[0]*5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if i == 2 or j == 2:
                    p[i][j] = col
        return p
    def pat_cross(col):
        p = [[0]*5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if i in (1,3) and j in (0,2,4) or i == 2:
                    p[i][j] = col
        return p
    def pat_hollow(col):
        p = [[0]*5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if i in (0,4) or j in (0,4):
                    p[i][j] = col
        return p
    for i in range(B):
        rowcols = [blocks[i][j][0][1] for j in range(C)]
        sr = sorted(rowcols)
        for j in range(C):
            col = rowcols[j]
            sub = blocks[i][j]
            interior = any(sub[x][y] != 0 and not (x in (0,4) or y in (0,4)) for x in range(5) for y in range(5))
            if not interior:
                if col == sr[-1]:
                    new = pat_plus(col)
                elif col == sr[0]:
                    new = pat_hollow(col)
                else:
                    new = pat_cross(col)
                for x in range(5):
                    for y in range(5):
                        if new[x][y] != 0:
                            blocks[i][j][x][y] = new[x][y]
    out = [row[:] for row in grid]
    for i, (r0, r1) in enumerate(br):
        for j, (c0, c1) in enumerate(bc):
            for x in range(r0, r1):
                for y in range(c0, c1):
                    out[x][y] = blocks[i][j][x-r0][y-c0]
    return out