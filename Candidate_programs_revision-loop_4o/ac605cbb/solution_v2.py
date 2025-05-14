def solve(grid):
    rows, cols = len(grid), len(grid[0])
    output = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                color = grid[r][c]
                if r + 1 < rows and grid[r + 1][c] == 0:
                    output[r + 1][c] = 5
                if r - 1 >= 0 and grid[r - 1][c] == 0:
                    output[r - 1][c] = 5
                if c + 1 < cols and grid[r][c + 1] == 0:
                    output[r][c + 1] = 5
                if c - 1 >= 0 and grid[r][c - 1] == 0:
                    output[r][c - 1] = 5
                output[r][c] = color
    return output