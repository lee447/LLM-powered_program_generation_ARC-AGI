from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def shift_row(row):
        non_zero_elements = [x for x in row if x != 0]
        zero_elements = [0] * (len(row) - len(non_zero_elements))
        return zero_elements + non_zero_elements

    def shift_grid(grid):
        return [shift_row(row) for row in grid]

    def transpose(grid):
        return [list(row) for row in zip(*grid)]

    transposed_grid = transpose(grid)
    shifted_transposed_grid = shift_grid(transposed_grid)
    return transpose(shifted_transposed_grid)