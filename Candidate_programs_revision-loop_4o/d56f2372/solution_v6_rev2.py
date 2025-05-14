from typing import List
import numpy as np

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_largest_connected_component(grid):
        visited = set()
        max_size = 0
        best_block = None

        def dfs(r, c, color):
            stack = [(r, c)]
            component = []
            while stack:
                x, y = stack.pop()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                component.append((x, y))
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == color and (nx, ny) not in visited:
                        stack.append((nx, ny))
            return component

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 and (r, c) not in visited:
                    component = dfs(r, c, grid[r][c])
                    if len(component) > max_size:
                        max_size = len(component)
                        best_block = component

        return best_block

    largest_component = find_largest_connected_component(grid)
    if not largest_component:
        return []

    min_row = min(x for x, y in largest_component)
    max_row = max(x for x, y in largest_component)
    min_col = min(y for x, y in largest_component)
    max_col = max(y for x, y in largest_component)

    result = [[0] * (max_col - min_col + 1) for _ in range(max_row - min_row + 1)]
    for x, y in largest_component:
        result[x - min_row][y - min_col] = grid[x][y]

    return result