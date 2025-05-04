def solve(grid):
    m = len(grid)
    pattern = [(r, c) for r in range(m) for c in range(m) if grid[r][c] != 0]
    if not pattern:
        return [[0] * (m*m) for _ in range(m*m)]
    color = grid[pattern[0][0]][pattern[0][1]]
    out = [[0] * (m*m) for _ in range(m*m)]
    for br, bc in pattern:
        for dr, dc in pattern:
            out[br*m + dr][bc*m + dc] = color
    return out