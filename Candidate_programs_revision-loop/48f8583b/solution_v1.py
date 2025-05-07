def solve(grid):
    N = len(grid)
    counts = {}
    for row in grid:
        for v in row:
            counts[v] = counts.get(v, 0) + 1
    minc = min(counts.values())
    out = [[0] * (N * N) for _ in range(N * N)]
    for i in range(N):
        for j in range(N):
            if counts[grid[i][j]] == minc:
                for di in range(N):
                    for dj in range(N):
                        out[i * N + di][j * N + dj] = grid[di][dj]
    return out