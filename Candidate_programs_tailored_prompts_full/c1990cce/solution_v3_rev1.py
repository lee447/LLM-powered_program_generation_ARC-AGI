def solve(grid):
    N = len(grid[0])
    c = grid[0].index(2)
    out = [[0]*N for _ in range(N)]
    for r in range(N):
        j1 = c - r
        if 0 <= j1 < N:
            out[r][j1] = 2
        j2 = c + r
        if 0 <= j2 < N:
            out[r][j2] = 2
    k = 2 - (c % 2)
    for r in range(N):
        left = c - r
        if left < 0:
            left = 0
        right = c + r
        if right >= N:
            right = N - 1
        for j in range(left, right+1):
            if out[r][j] == 0 and (r - j) % 4 == k:
                out[r][j] = 1
    return out