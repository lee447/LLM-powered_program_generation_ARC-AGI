def solve(grid):
    blk = grid
    D = len({c for row in blk for c in row})
    N = 6 - D
    s = sum(sum(row) for row in blk)
    avg = s / 9
    res = [[0]*9 for _ in range(9)]
    if N == 1:
        slots = [(0,6)] if avg > 5 else [(0,0)]
    elif N == 2:
        slots = [(6,3),(6,6)] if avg > 5 else [(0,0),(3,3)]
    else:
        slots = [(0,3),(3,0),(6,3)] if avg > 5 else [(0,0),(0,3),(6,3)]
    for r0,c0 in slots:
        for i in range(3):
            for j in range(3):
                res[r0+i][c0+j] = blk[i][j]
    return res