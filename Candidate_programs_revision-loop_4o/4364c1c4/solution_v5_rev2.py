from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_non_background_color(row):
        for color in row:
            if color != background_color:
                return color
        return None

    def shift_row(row, color):
        new_row = [background_color] * len(row)
        color_indices = [i for i, x in enumerate(row) if x == color]
        if color_indices:
            start = color_indices[0]
            end = color_indices[-1]
            new_row[start:end+1] = [color] * (end - start + 1)
        return new_row

    background_color = grid[0][0]
    result = [row[:] for row in grid]

    for i in range(len(grid)):
        non_bg_color = find_non_background_color(grid[i])
        if non_bg_color is not None:
            result[i] = shift_row(grid[i], non_bg_color)

    return result