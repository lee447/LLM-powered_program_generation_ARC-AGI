from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def transform_color(color):
        return color + 1

    def process_row(row):
        new_row = row[:]
        i = 0
        while i < len(row) - 1:
            if row[i] == row[i + 1] and row[i] != 0:
                new_row[i] = transform_color(row[i])
                new_row[i + 1] = transform_color(row[i + 1])
                i += 1
            i += 1
        return new_row

    return [process_row(row) for row in grid]