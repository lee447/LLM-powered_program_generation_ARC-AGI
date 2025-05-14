from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def extract_subgrid(grid, start_col, end_col):
        return [row[start_col:end_col] for row in grid]

    def find_non_zero_columns(grid):
        num_cols = len(grid[0])
        non_zero_cols = []
        for col in range(num_cols):
            if any(row[col] != 0 for row in grid):
                non_zero_cols.append(col)
        return non_zero_cols

    non_zero_cols = find_non_zero_columns(grid)
    start_col = non_zero_cols[0]
    end_col = non_zero_cols[-1] + 1

    subgrid = extract_subgrid(grid, start_col, end_col)
    
    def find_non_zero_rows(grid):
        non_zero_rows = []
        for row in grid:
            if any(cell != 0 for cell in row):
                non_zero_rows.append(row)
        return non_zero_rows

    subgrid = find_non_zero_rows(subgrid)
    
    def transpose(grid):
        return list(map(list, zip(*grid)))

    transposed_subgrid = transpose(subgrid)
    non_zero_cols_transposed = find_non_zero_columns(transposed_subgrid)
    start_col_transposed = non_zero_cols_transposed[0]
    end_col_transposed = non_zero_cols_transposed[-1] + 1

    final_subgrid = extract_subgrid(transposed_subgrid, start_col_transposed, end_col_transposed)
    return transpose(final_subgrid)