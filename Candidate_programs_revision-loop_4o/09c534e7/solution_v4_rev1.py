from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def fill_region(x, y, target_color, new_color):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return
        if grid[x][y] != target_color:
            return
        grid[x][y] = new_color
        fill_region(x + 1, y, target_color, new_color)
        fill_region(x - 1, y, target_color, new_color)
        fill_region(x, y + 1, target_color, new_color)
        fill_region(x, y - 1, target_color, new_color)

    def find_and_fill():
        color_map = {}
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] != 0:
                    target_color = grid[x][y]
                    if target_color not in color_map:
                        new_color = len(color_map) + 1
                        color_map[target_color] = new_color
                        fill_region(x, y, target_color, new_color)

    find_and_fill()
    return grid