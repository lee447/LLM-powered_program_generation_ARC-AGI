from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    input_row = grid[0]
    n = len(input_row)
    output_grid = [input_row[:]]
    for i in range(1, n):
        new_row = [0] * n
        for j in range(n):
            if j - i >= 0 and j + i < n:
                new_row[j - i] = input_row[j]
                new_row[j + i] = input_row[j]
        output_grid.append(new_row)
    return output_grid