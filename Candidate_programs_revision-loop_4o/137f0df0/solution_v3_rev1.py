def solve(grid):
    rows, cols = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    for r in range(0, rows, 3):
        for c in range(0, cols, 3):
            if r + 2 < rows and c + 2 < cols:
                for i in range(3):
                    result[r + i][c + 2] = 2
                for j in range(3):
                    result[r + 2][c + j] = 2
                result[r + 2][c + 2] = 1
                result[r + 2][c] = 1
                result[r][c + 2] = 2
    return result