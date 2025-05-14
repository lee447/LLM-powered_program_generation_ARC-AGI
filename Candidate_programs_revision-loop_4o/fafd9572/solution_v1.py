from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def transform_color(color):
        if color == 1:
            return 2
        elif color == 2:
            return 3
        elif color == 3:
            return 4
        elif color == 4:
            return 5
        return color

    def process_row(row):
        new_row = row[:]
        for i in range(len(row) - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                new_row[i] = transform_color(row[i])
                new_row[i + 1] = transform_color(row[i + 1])
        return new_row

    return [process_row(row) for row in grid]