def solve(grid):
    m = len(grid)
    zeros = [(r, c) for r in range(m) for c in range(m) if grid[r][c] == 0]
    color = next(grid[r][c] for r in range(m) for c in range(m) if grid[r][c] != 0)
    out = [[0] * (m * m) for _ in range(m * m)]
    for br, bc in zeros:
        for dr, dc in zeros:
            out[br * m + dr][bc * m + dc] = color
    return out