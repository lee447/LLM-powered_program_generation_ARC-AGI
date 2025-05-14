from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def fill_eights(grid, start_row, start_col):
        stack = [(start_row, start_col)]
        while stack:
            row, col = stack.pop()
            if grid[row][col] == 3:
                grid[row][col] = 8
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 3:
                        stack.append((new_row, new_col))

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 3:
                fill_eights(grid, row, col)
    return grid