from typing import List
import numpy as np

def solve(grid: List[List[int]]) -> List[List[int]]:
    grid = np.array(grid)
    unique_colors = set(grid.flatten()) - {0}
    color_map = {color: idx + 1 for idx, color in enumerate(unique_colors)}
    
    def fill_region(x, y, target_color, new_color):
        if grid[x, y] != target_color:
            return
        grid[x, y] = new_color
        if x > 0:
            fill_region(x - 1, y, target_color, new_color)
        if x < grid.shape[0] - 1:
            fill_region(x + 1, y, target_color, new_color)
        if y > 0:
            fill_region(x, y - 1, target_color, new_color)
        if y < grid.shape[1] - 1:
            fill_region(x, y + 1, target_color, new_color)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] != 0:
                target_color = grid[i, j]
                new_color = color_map[target_color]
                if new_color != target_color:
                    fill_region(i, j, target_color, new_color)
    
    return grid.tolist()