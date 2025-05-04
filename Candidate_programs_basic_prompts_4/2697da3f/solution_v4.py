def solve(grid):
    h, w = len(grid), len(grid[0])
    pts = [(i, j) for i in range(h) for j in range(w) if grid[i][j] != 0]
    if not pts:
        return grid
    r0 = min(i for i, _ in pts)
    r1 = max(i for i, _ in pts)
    c0 = min(j for _, j in pts)
    c1 = max(j for _, j in pts)
    ph = r1 - r0 + 1
    pw = c1 - c0 + 1
    p = [row[c0:c0+pw] for row in grid[r0:r0+ph]]
    def rot90(m):
        return [list(row) for row in zip(*m[::-1])]
    def rot180(m):
        return [row[::-1] for row in m[::-1]]
    def rot270(m):
        return [list(row) for row in zip(*m)][::-1]
    r0p = p
    r90 = rot90(p)
    r180 = rot180(p)
    r270 = rot270(p)
    border = (ph//2) % 2
    out_h = ph*3 + 2*border
    out_w = pw*3 + 2*border
    out = [[0]*out_w for _ in range(out_h)]
    blocks = { (1,0):r0p, (0,1):r90, (1,2):r180, (2,1):r270 }
    for (bi, bj), mat in blocks.items():
        sr = border + bi*ph
        sc = border + bj*pw
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                v = mat[i][j]
                if v:
                    out[sr+i][sc+j] = v
    return out