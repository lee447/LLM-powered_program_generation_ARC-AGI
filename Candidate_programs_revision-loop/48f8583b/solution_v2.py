def solve(grid):
    n = len(grid)
    N = n * n
    freq = {}
    for row in grid:
        for v in row:
            freq[v] = freq.get(v, 0) + 1
    minf = min(freq.values())
    out = [[0] * N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if freq[grid[i][j]] == minf:
                for di in range(n):
                    for dj in range(n):
                        out[i*n + di][j*n + dj] = grid[di][dj]
    return out