def solve(grid):
    rows, cols = len(grid), len(grid[0])
    output = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                for i in range(4):
                    if r + i < rows:
                        output[r + i][c] = grid[r][c]
                break
    return output