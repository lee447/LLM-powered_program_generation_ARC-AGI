from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_pattern(grid):
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                if grid[r][c] == 0 and grid[r][c+1] == 8 and grid[r][c+2] == 0:
                    if grid[r+1][c] == 8 and grid[r+1][c+1] == 1 and grid[r+1][c+2] == 8:
                        if grid[r+2][c] == 0 and grid[r+2][c+1] == 8 and grid[r+2][c+2] == 0:
                            return r, c
        return None

    def apply_pattern(grid, r, c):
        grid[r][c] = 0
        grid[r][c+1] = 0
        grid[r][c+2] = 0
        grid[r+1][c] = 0
        grid[r+1][c+1] = 0
        grid[r+1][c+2] = 0
        grid[r+2][c] = 4
        grid[r+2][c+1] = 4
        grid[r+2][c+2] = 4

    while True:
        pattern_pos = find_pattern(grid)
        if pattern_pos is None:
            break
        apply_pattern(grid, *pattern_pos)

    return grid