from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    color_map = {
        0: [4, 1, 9],
        1: [4, 1, 9],
        2: [4, 1, 9],
        3: [4, 1, 9],
        4: [4, 1, 9],
        5: [3, 4, 9],
        6: [3, 4, 9],
        7: [3, 4, 9],
        8: [3, 4, 9],
        9: [3, 4, 9]
    }
    result = []
    for row in grid:
        new_row = []
        for i in range(0, len(row), 3):
            segment = row[i:i+3]
            if segment.count(5) >= 2:
                new_row.extend(color_map[5])
            else:
                new_row.extend(color_map[0])
        result.append(new_row)
    return result