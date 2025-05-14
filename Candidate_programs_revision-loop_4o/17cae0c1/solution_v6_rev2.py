from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    result = []
    for row in grid:
        new_row = []
        for i in range(0, len(row), 3):
            segment = row[i:i+3]
            if segment.count(5) == 3:
                new_row.extend([3, 3, 3])
            elif segment.count(5) == 2:
                new_row.extend([9, 9, 9])
            elif segment.count(5) == 1:
                new_row.extend([1, 1, 1])
            else:
                new_row.extend([4, 4, 4])
        result.append(new_row)
    return result