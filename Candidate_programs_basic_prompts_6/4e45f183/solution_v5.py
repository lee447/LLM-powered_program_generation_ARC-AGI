def solve(grid):
    h = len(grid)
    w = len(grid[0])
    bs = (h - 4) // 3
    sep = bs + 1
    def get_block(br, bc):
        r0 = 1 + br * sep
        c0 = 1 + bc * sep
        return [row[c0:c0+bs] for row in grid[r0:r0+bs]]
    def put_block(out, br, bc,	block):
        r0 = 1 + br * sep
        c0 = 1 + bc * sep
        for i in range(bs):
            for j in range(bs):
                out[r0+i][c0+j] = block[i][j]
    def rot90(b):
        return [list(row) for row in zip(*b[::-1])]
    out = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0:
                out[i][j] = 0
    for br in range(3):
        for bc in range(3):
            src = get_block(bc, br)
            dst = rot90(src)
            put_block(out, br, bc, dst)
    return out