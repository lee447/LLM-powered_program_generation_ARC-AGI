def solve(grid):
    N = len(grid[0])
    c = grid[0].index(2)
    out = [[0]*N for _ in range(N)]
    for r in range(N):
        if 0 <= c-r < N:
            out[r][c-r] = 2
        if 0 <= c+r < N:
            out[r][c+r] = 2
    for dr in range(1, N):
        r = N-1 - dr
        if 0 <= c - dr < N and out[r][c-dr] == 0:
            out[r][c-dr] = 1
        if 0 <= c + dr < N and out[r][c+dr] == 0:
            out[r][c+dr] = 1
    return out