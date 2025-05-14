from typing import List
import numpy as np

def solve(grid: List[List[int]]) -> List[List[int]]:
    def extract_blocks(grid):
        blocks = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 and (r, c) not in visited:
                    color = grid[r][c]
                    block = []
                    stack = [(r, c)]
                    while stack:
                        x, y = stack.pop()
                        if (x, y) not in visited and grid[x][y] == color:
                            visited.add((x, y))
                            block.append((x, y))
                            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                                    stack.append((nx, ny))
                    blocks.append((color, block))
        return blocks

    def transform_blocks(blocks):
        new_grid = np.zeros((8, 14), dtype=int)
        for color, block in blocks:
            min_r = min(r for r, c in block)
            min_c = min(c for r, c in block)
            for r, c in block:
                new_r = r - min_r
                new_c = c - min_c
                if new_r < new_grid.shape[0] and new_c < new_grid.shape[1]:
                    new_grid[new_r][new_c] = color
        return new_grid.tolist()

    blocks = extract_blocks(grid)
    return transform_blocks(blocks)