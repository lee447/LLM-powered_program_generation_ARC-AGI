from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_non_zero_blocks(grid):
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
                        if (cr, cc) in visited or grid[cr][cc] != color:
                            continue
                        visited.add((cr, cc))
                        block.append((cr, cc))
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                                queue.append((nr, nc))
                    blocks.append(block)
        return blocks

    def move_block_to_bottom_left(grid, block):
        min_r = min(r for r, c in block)
        min_c = min(c for r, c in block)
        max_r = max(r for r, c in block)
        max_c = max(c for r, c in block)
        height = max_r - min_r + 1
        width = max_c - min_c + 1

        new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
        for r, c in block:
            new_r = len(grid) - height + (r - min_r)
            new_c = c - min_c
            new_grid[new_r][new_c] = grid[r][c]
        return new_grid

    blocks = find_non_zero_blocks(grid)
    result_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for block in blocks:
        block_grid = move_block_to_bottom_left(grid, block)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if block_grid[r][c] != 0:
                    result_grid[r][c] = block_grid[r][c]
    return result_grid