from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def transform_color(color):
        return (color + 4) % 10

    def apply_transformation(grid):
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] != 4:
                    grid[r][c] = transform_color(grid[r][c])
        return grid

    return apply_transformation(grid)