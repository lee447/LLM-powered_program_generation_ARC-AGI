from typing import List
import numpy as np

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_largest_non_zero_area(grid):
        max_area = 0
        best_min_row, best_max_row, best_min_col, best_max_col = 0, 0, 0, 0
        visited = set()
        
        def dfs(r, c):
            stack = [(r, c)]
            min_row, max_row, min_col, max_col = r, r, c, c
            while stack:
                x, y = stack.pop()
                if (x, y) in visited or grid[x][y] == 0:
                    continue
                visited.add((x, y))
                min_row, max_row = min(min_row, x), max(max_row, x)
                min_col, max_col = min(min_col, y), max(max_col, y)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                        stack.append((nx, ny))
            return min_row, max_row, min_col, max_col

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 and (r, c) not in visited:
                    min_row, max_row, min_col, max_col = dfs(r, c)
                    area = (max_row - min_row + 1) * (max_col - min_col + 1)
                    if area > max_area:
                        max_area = area
                        best_min_row, best_max_row, best_min_col, best_max_col = min_row, max_row, min_col, max_col
        return best_min_row, best_max_row, best_min_col, best_max_col

    min_row, max_row, min_col, max_col = find_largest_non_zero_area(grid)
    result = []
    for r in range(min_row, max_row + 1):
        result.append(grid[r][min_col:max_col + 1])
    return result