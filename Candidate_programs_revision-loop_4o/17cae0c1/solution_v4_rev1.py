from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    color_map = {
        0: [4, 4, 4],
        1: [4, 4, 4],
        2: [4, 4, 4],
        3: [4, 4, 4],
        4: [4, 4, 4],
        5: [3, 3, 3],
        6: [3, 3, 3],
        7: [3, 3, 3],
        8: [3, 3, 3],
        9: [3, 3, 3]
    }
    result = []
    for row in grid:
        new_row = []
        for i in range(0, len(row), 3):
            segment = row[i:i+3]
            if segment.count(5) == 3:
                new_row.extend([6, 6, 6])
            elif segment.count(5) == 2:
                new_row.extend([3, 3, 3])
            elif segment.count(5) == 1:
                new_row.extend([1, 1, 1])
            else:
                new_row.extend([4, 4, 4])
        result.append(new_row)
    return result