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
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] != 0:
                    target_color = grid[x][y]
                    new_color = target_color + 1
                    fill_region(x, y, target_color, new_color)
                    return

    find_and_fill()
    return grid