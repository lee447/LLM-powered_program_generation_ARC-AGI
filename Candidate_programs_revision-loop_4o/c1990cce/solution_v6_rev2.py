from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    input_row = grid[0]
    n = len(input_row)
    output_grid = [input_row[:]]
    for i in range(1, n):
        new_row = [0] * n
        for j in range(n):
            if input_row[j] != 0:
                if j - i >= 0:
                    new_row[j - i] = input_row[j]
                if j + i < n:
                    new_row[j + i] = input_row[j]
        if i < n // 2:
            for j in range(n):
                if new_row[j] == 0 and (j - 1 >= 0 and new_row[j - 1] != 0) and (j + 1 < n and new_row[j + 1] != 0):
                    new_row[j] = 1
        output_grid.append(new_row)
    return output_grid