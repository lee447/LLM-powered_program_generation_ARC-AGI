from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_non_background_color(row):
        for color in row:
            if color != background_color:
                return color
        return background_color

    def shift_row(row, color):
        new_row = [background_color] * len(row)
        start = row.index(color)
        end = len(row) - row[::-1].index(color)
        new_row[start-1:end-1] = row[start:end]
        return new_row

    background_color = grid[0][0]
    result = [row[:] for row in grid]

    for i in range(len(grid)):
        non_bg_color = find_non_background_color(grid[i])
        if non_bg_color != background_color:
            result[i] = shift_row(grid[i], non_bg_color)

    return result