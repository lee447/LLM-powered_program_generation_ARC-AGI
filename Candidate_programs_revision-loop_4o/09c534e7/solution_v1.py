def solve(grid):
    def fill_region(x, y, target_color, new_color):
        if grid[x][y] != target_color:
            return
        grid[x][y] = new_color
        if x > 0:
            fill_region(x - 1, y, target_color, new_color)
        if x < len(grid) - 1:
            fill_region(x + 1, y, target_color, new_color)
        if y > 0:
            fill_region(x, y - 1, target_color, new_color)
        if y < len(grid[0]) - 1:
            fill_region(x, y + 1, target_color, new_color)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                target_color = grid[i][j]
                new_color = target_color
                if i > 0 and grid[i - 1][j] != 0 and grid[i - 1][j] != target_color:
                    new_color = grid[i - 1][j]
                elif j > 0 and grid[i][j - 1] != 0 and grid[i][j - 1] != target_color:
                    new_color = grid[i][j - 1]
                elif i < len(grid) - 1 and grid[i + 1][j] != 0 and grid[i + 1][j] != target_color:
                    new_color = grid[i + 1][j]
                elif j < len(grid[0]) - 1 and grid[i][j + 1] != 0 and grid[i][j + 1] != target_color:
                    new_color = grid[i][j + 1]
                if new_color != target_color:
                    fill_region(i, j, target_color, new_color)
    return grid