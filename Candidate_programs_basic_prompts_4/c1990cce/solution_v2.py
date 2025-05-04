def solve(grid):
    n = len(grid[0])
    seed = grid[0].index(2)
    mid = n // 2
    out = [[0] * n for _ in range(n)]
    for r in range(n):
        if r <= mid:
            for d in (-1, 1):
                c = seed + d * r
                if 0 <= c < n:
                    out[r][c] = 2
        if r > 0:
            d = r - 1
            for d0 in (-1, 1):
                c = seed + d * d0
                if 0 <= c < n and out[r][c] == 0:
                    out[r][c] = 1
    return out