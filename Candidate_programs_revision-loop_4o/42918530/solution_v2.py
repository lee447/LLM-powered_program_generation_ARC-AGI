from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def fill_pattern(row, start, end, color):
        for i in range(start, end):
            if row[i] == 0:
                row[i] = color

    for row in grid:
        start = None
        color = None
        for i, val in enumerate(row):
            if val != 0:
                if start is None:
                    start = i
                    color = val
                elif val != color:
                    fill_pattern(row, start, i, color)
                    start = i
                    color = val
        if start is not None:
            fill_pattern(row, start, len(row), color)
    
    return grid