from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def fill_row(row):
        new_row = row[:]
        for i in range(1, len(row) - 1):
            if row[i] != 0 and row[i - 1] == 0 and row[i + 1] == 0:
                new_row[i] = 0
        return new_row

    return [fill_row(row) for row in grid]