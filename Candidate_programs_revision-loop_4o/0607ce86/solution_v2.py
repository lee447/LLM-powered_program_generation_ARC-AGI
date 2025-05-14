from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def is_row_empty(row):
        return all(cell == 0 for cell in row)
    
    def is_row_filled(row):
        return all(cell != 0 for cell in row)
    
    def process_row(row):
        if is_row_empty(row) or is_row_filled(row):
            return row
        first_non_zero = next((i for i, x in enumerate(row) if x != 0), None)
        last_non_zero = next((i for i, x in enumerate(reversed(row)) if x != 0), None)
        if last_non_zero is not None:
            last_non_zero = len(row) - 1 - last_non_zero
        if first_non_zero is not None and last_non_zero is not None:
            fill_value = row[first_non_zero]
            for i in range(first_non_zero, last_non_zero + 1):
                row[i] = fill_value
        return row
    
    return [process_row(row) for row in grid]