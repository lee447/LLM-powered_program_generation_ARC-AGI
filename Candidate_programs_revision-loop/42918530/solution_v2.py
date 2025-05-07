def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    B, S = 5, 1 + (w - 5) // 2
    def inside(r0, c0, i, j): return r0+1 <= i < r0+4 and c0+1 <= j < c0+4
    def fill(r0, c0, shape, c):
        if shape == 'dot':
            res[r0+2][c0+2] = c
        elif shape == 'h':
            for dc in range(1,4): res[r0+2][c0+dc] = c
        elif shape == 'v':
            for dr in range(1,4): res[r0+dr][c0+2] = c
        elif shape == '+':
            for dr in range(1,4): res[r0+dr][c0+2] = c
            for dc in range(1,4): res[r0+2][c0+dc] = c
    shapes = {2:'h',4:'+',6:'v',8:'h',3:'v',1:'dot'}
    rows = (h - 5) // 6 + 1
    cols = (w - 5) // 6 + 1
    for bi in range(rows):
        r0 = bi * 6
        for bj in range(cols):
            c0 = bj * 6
            c = grid[r0][c0+1]
            if c in shapes:
                empty = True
                for i in range(r0+1, r0+4):
                    for j in range(c0+1, c0+4):
                        if grid[i][j] != 0: empty = False
                if empty:
                    fill(r0, c0, shapes[c], c)
    return res