def solve(grid):
    def is_red_block(i, j):
        return (grid[i][j] == 2 and
                (i == 0 or grid[i-1][j] != 2) and
                (j == 0 or grid[i][j-1] != 2) and
                (i+1 < len(grid) and grid[i+1][j] == 2) and
                (j+1 < len(grid[0]) and grid[i][j+1] == 2))

    def is_green_block(i, j):
        return (grid[i][j] == 3 and
                (i == 0 or grid[i-1][j] != 3) and
                (j == 0 or grid[i][j-1] != 3) and
                (i+1 < len(grid) and grid[i+1][j] == 3) and
                (j+1 < len(grid[0]) and grid[i][j+1] == 3))

    output = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_red_block(i, j):
                output[0][0] = 1
            if is_green_block(i, j):
                output[1][1] = 1
    return output