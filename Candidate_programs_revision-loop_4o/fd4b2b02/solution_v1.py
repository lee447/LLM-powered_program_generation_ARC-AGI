def solve(grid):
    n, m = len(grid), len(grid[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                if i + 1 < n and grid[i + 1][j] == grid[i][j]:
                    for k in range(i, n):
                        if grid[k][j] == grid[i][j]:
                            result[k][j] = grid[i][j]
                        else:
                            break
                if j + 1 < m and grid[i][j + 1] == grid[i][j]:
                    for k in range(j, m):
                        if grid[i][k] == grid[i][j]:
                            result[i][k] = grid[i][j]
                        else:
                            break
    return result