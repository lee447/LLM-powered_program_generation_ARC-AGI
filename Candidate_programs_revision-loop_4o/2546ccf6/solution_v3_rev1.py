def solve(grid):
    rows, cols = len(grid), len(grid[0])
    result = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                result[i][j] = grid[i][j]
            else:
                if i > 0 and result[i-1][j] != 0:
                    result[i][j] = result[i-1][j]
                elif j > 0 and result[i][j-1] != 0:
                    result[i][j] = result[i][j-1]
    
    return result