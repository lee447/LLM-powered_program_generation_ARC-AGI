from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_non_zero_bounds(grid):
        min_row, max_row, min_col, max_col = len(grid), 0, len(grid[0]), 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
        return min_row, max_row, min_col, max_col

    min_row, max_row, min_col, max_col = find_non_zero_bounds(grid)
    cropped_grid = [row[min_col:max_col+1] for row in grid[min_row:max_row+1]]
    
    def find_largest_non_zero_block(grid):
        max_area = 0
        best_block = None
        for start_row in range(len(grid)):
            for start_col in range(len(grid[0])):
                if grid[start_row][start_col] != 0:
                    for end_row in range(start_row, len(grid)):
                        for end_col in range(start_col, len(grid[0])):
                            if grid[end_row][end_col] != 0:
                                block = [row[start_col:end_col+1] for row in grid[start_row:end_row+1]]
                                if all(any(cell != 0 for cell in row) for row in block):
                                    area = (end_row - start_row + 1) * (end_col - start_col + 1)
                                    if area > max_area:
                                        max_area = area
                                        best_block = block
        return best_block

    def find_largest_connected_block(grid):
        visited = set()
        def dfs(r, c, color):
            stack = [(r, c)]
            block = []
            while stack:
                x, y = stack.pop()
                if (x, y) in visited or grid[x][y] != color:
                    continue
                visited.add((x, y))
                block.append((x, y))
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                        stack.append((nx, ny))
            return block

        max_block = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 and (r, c) not in visited:
                    block = dfs(r, c, grid[r][c])
                    if len(block) > len(max_block):
                        max_block = block

        if not max_block:
            return []

        min_r = min(x for x, y in max_block)
        max_r = max(x for x, y in max_block)
        min_c = min(y for x, y in max_block)
        max_c = max(y for x, y in max_block)

        result = [[0] * (max_c - min_c + 1) for _ in range(max_r - min_r + 1)]
        for x, y in max_block:
            result[x - min_r][y - min_c] = grid[x][y]

        return result

    return find_largest_connected_block(cropped_grid)