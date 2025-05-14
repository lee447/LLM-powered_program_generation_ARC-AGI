from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    input_row = grid[0]
    n = len(input_row)
    output_grid = [input_row[:]]
    
    for i in range(1, n):
        new_row = [0] * n
        for j in range(n):
            if j - i >= 0 and j + i < n:
                if input_row[j] == 2:
                    new_row[j - i] = 2
                    new_row[j + i] = 2
                elif input_row[j] == 1:
                    new_row[j] = 1
        output_grid.append(new_row)
    
    return output_grid