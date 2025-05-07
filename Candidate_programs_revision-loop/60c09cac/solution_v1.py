def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [[0] * (cols * 2) for _ in range(rows * 2)]
    for i in range(rows):
        for j in range(cols):
            v = grid[i][j]
            r, c = i * 2, j * 2
            result[r][c] = v
            result[r][c + 1] = v
            result[r + 1][c] = v
            result[r + 1][c + 1] = v
    return result