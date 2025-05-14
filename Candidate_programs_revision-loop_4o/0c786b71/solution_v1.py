from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def mirror_and_expand(row):
        return row + row[::-1]

    def expand_grid(grid):
        expanded = []
        for row in grid:
            expanded.append(mirror_and_expand(row))
        for row in grid[::-1]:
            expanded.append(mirror_and_expand(row))
        return expanded

    return expand_grid(grid)