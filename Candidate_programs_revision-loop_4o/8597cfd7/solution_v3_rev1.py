from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    color_count = {}
    for row in grid:
        for color in row:
            if color != 0:
                if color in color_count:
                    color_count[color] += 1
                else:
                    color_count[color] = 1
    max_color = max(color_count, key=lambda x: (color_count[x], -x))
    return [[max_color, max_color], [max_color, max_color]]