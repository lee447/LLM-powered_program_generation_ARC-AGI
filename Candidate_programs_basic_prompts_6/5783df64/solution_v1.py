def solve(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    bs = n // 3
    res = [[0] * 3 for _ in range(3)]
    for bi in range(3):
        for bj in range(3):
            for i in range(bi * bs, (bi + 1) * bs):
                for j in range(bj * bs, (bj + 1) * bs):
                    v = grid[i][j]
                    if v:
                        res[bi][bj] = v
                        break
                if res[bi][bj]:
                    break
    return res