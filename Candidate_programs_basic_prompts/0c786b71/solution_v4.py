def solve(grid):
    R = len(grid)
    C = len(grid[0])
    newR = 2 * R
    newC = 2 * C
    out = [[0] * newC for _ in range(newR)]
    for i in range(newR):
        ii = i if i < R else newR - 1 - i
        for j in range(newC):
            jj = j if j < C else newC - 1 - j
            out[i][j] = grid[R - 1 - ii][C - 1 - jj]
    return out