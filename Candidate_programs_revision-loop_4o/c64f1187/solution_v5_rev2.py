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
                    queue = [(r, c)]
                    while queue:
                        cr, cc = queue.pop(0)
                        if (cr, cc) not in visited and grid[cr][cc] == color:
                            visited.add((cr, cc))
                            block.append((cr, cc))
                            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nr, nc = cr + dr, cc + dc
                                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                                    queue.append((nr, nc))
                    blocks.append((color, block))
        return blocks

    def place_blocks(blocks, output_grid):
        for color, block in blocks:
            min_r = min(r for r, c in block)
            min_c = min(c for r, c in block)
            for r, c in block:
                output_grid[r - min_r][c - min_c] = color

    blocks = extract_blocks(grid)
    max_r = max(r for color, block in blocks for r, c in block)
    max_c = max(c for color, block in blocks for r, c in block)
    output_grid = [[0] * (max_c + 1) for _ in range(max_r + 1)]
    place_blocks(blocks, output_grid)
    
    # Trim the output grid to remove empty rows and columns
    output_grid = np.array(output_grid)
    non_empty_rows = np.any(output_grid != 0, axis=1)
    non_empty_cols = np.any(output_grid != 0, axis=0)
    trimmed_grid = output_grid[np.ix_(non_empty_rows, non_empty_cols)]
    
    return trimmed_grid.tolist()