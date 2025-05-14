from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_pattern(grid):
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                if grid[r][c] == 0 and grid[r][c+1] == 0 and grid[r][c+2] == 0 and \
                   grid[r+1][c] == 0 and grid[r+1][c+1] == 8 and grid[r+1][c+2] == 0 and \
                   grid[r+2][c] == 0 and grid[r+2][c+1] == 0 and grid[r+2][c+2] == 0:
                    return r, c
        return None, None

    def apply_pattern(grid, r, c):
        if r is not None and c is not None:
            grid[r][c] = 0
            grid[r][c+1] = 0
            grid[r][c+2] = 0
            grid[r+1][c] = 0
            grid[r+1][c+1] = 0
            grid[r+1][c+2] = 0
            grid[r+2][c] = 0
            grid[r+2][c+1] = 0
            grid[r+2][c+2] = 0

    r, c = find_pattern(grid)
    apply_pattern(grid, r, c)
    return grid