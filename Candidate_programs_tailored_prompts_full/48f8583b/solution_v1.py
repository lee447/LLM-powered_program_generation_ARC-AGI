def solve(grid):
    n = len(grid)
    counts = {}
    for row in grid:
        for v in row:
            counts[v] = counts.get(v, 0) + 1
    rare = min(counts.items(), key=lambda x: (x[1], x[0]))[0]
    positions = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == rare]
    out = [[0] * (n * 3) for _ in range(n * 3)]
    for br, bc in positions:
        for i in range(n):
            for j in range(n):
                out[br * n + i][bc * n + j] = grid[i][j]
    return out