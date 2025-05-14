from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    color_map = {
        0: [4, 4, 4],
        5: [3, 3, 3],
        9: [6, 6, 6],
        'other': [1, 1, 1]
    }
    result = []
    for row in grid:
        new_row = []
        for i in range(0, len(row), 3):
            segment = row[i:i+3]
            if segment.count(5) >= 2:
                new_row.extend(color_map[5])
            elif segment.count(0) >= 2:
                new_row.extend(color_map[0])
            elif segment.count(9) >= 2:
                new_row.extend(color_map[9])
            else:
                new_row.extend(color_map['other'])
        result.append(new_row)
    return result