def solve(grid):
    rows, cols = len(grid), len(grid[0])
    result = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 5:
                result[r][c] = 5
            elif grid[r][c] == 2:
                if r > 0 and grid[r-1][c] == 5:
                    result[r][c] = 2
                elif r < rows - 1 and grid[r+1][c] == 5:
                    result[r][c] = 2
                elif c > 0 and grid[r][c-1] == 5:
                    result[r][c] = 2
                elif c < cols - 1 and grid[r][c+1] == 5:
                    result[r][c] = 2
    return result