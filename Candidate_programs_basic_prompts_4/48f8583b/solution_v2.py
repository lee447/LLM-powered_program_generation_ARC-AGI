def solve(grid):
    R, C = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for v in row:
            counts[v] = counts.get(v, 0) + 1
    min_count = min(counts.values())
    color = min(v for v, c in counts.items() if c == min_count)
    positions = [(i, j) for i in range(R) for j in range(C) if grid[i][j] == color]
    out = [[0] * (C * C) for _ in range(R * R)]
    for br, bc in positions:
        for i in range(R):
            for j in range(C):
                out[br * R + i][bc * C + j] = grid[i][j]
    return out