def solve(grid):
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 7:
                subgrid = []
                for x in range(i, n):
                    if grid[x][j] != 7:
                        subgrid.append(grid[x][j:j+8])
                return subgrid
    return grid