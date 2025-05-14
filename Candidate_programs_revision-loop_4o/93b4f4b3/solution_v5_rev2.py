def solve(grid):
    n = len(grid)
    m = len(grid[0])
    output_grid = [[0] * (m // 2) for _ in range(n)]
    
    for i in range(n):
        for j in range(m // 2):
            output_grid[i][j] = grid[i][j]
    
    for i in range(0, n, 4):
        for j in range(0, m, 6):
            subgrid = [row[j:j+6] for row in grid[i:i+4]]
            for x in range(min(4, n - i)):
                for y in range(min(6, m - j)):
                    if subgrid[x][y] != 0:
                        output_grid[i + x][j // 2 + y % 3] = subgrid[x][y]
    
    return output_grid