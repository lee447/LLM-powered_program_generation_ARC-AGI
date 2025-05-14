from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    color_map = {1: 2, 2: 3, 3: 4, 4: 5}
    output = []
    for row in grid:
        new_row = []
        for cell in row:
            if cell in color_map:
                new_row.append(color_map[cell])
            else:
                new_row.append(cell)
        output.append(new_row)
    return output