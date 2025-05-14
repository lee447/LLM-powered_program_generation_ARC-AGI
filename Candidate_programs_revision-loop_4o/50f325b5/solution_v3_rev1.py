def solve(grid):
    def flood_fill(x, y, target_color, replacement_color):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return
        if grid[x][y] != target_color:
            return
        grid[x][y] = replacement_color
        flood_fill(x + 1, y, target_color, replacement_color)
        flood_fill(x - 1, y, target_color, replacement_color)
        flood_fill(x, y + 1, target_color, replacement_color)
        flood_fill(x, y - 1, target_color, replacement_color)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 8:
                flood_fill(i, j, 8, 3)
    return grid