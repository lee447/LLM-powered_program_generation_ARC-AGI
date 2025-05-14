def solve(grid):
    def fill_around(x, y, target_color, new_color):
        if x > 0 and grid[x-1][y] == target_color:
            grid[x-1][y] = new_color
        if x < len(grid) - 1 and grid[x+1][y] == target_color:
            grid[x+1][y] = new_color
        if y > 0 and grid[x][y-1] == target_color:
            grid[x][y-1] = new_color
        if y < len(grid[x]) - 1 and grid[x][y+1] == target_color:
            grid[x][y+1] = new_color

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 4:
                fill_around(i, j, 0, 8)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 8:
                fill_around(i, j, 0, 7)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 8:
                grid[i][j] = 0

    return grid