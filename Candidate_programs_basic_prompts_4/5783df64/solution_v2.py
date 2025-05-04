def solve(grid):
    n = len(grid)
    m = len(grid[0])
    bh = n // 3
    bw = m // 3
    result = [[0] * 3 for _ in range(3)]
    for bi in range(3):
        for bj in range(3):
            for i in range(bi * bh, (bi + 1) * bh):
                for j in range(bj * bw, (bj + 1) * bw):
                    if grid[i][j] != 0:
                        result[bi][bj] = grid[i][j]
                        break
                if result[bi][bj] != 0:
                    break
    return result