from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_blocks(grid):
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

    def shift_block(block, direction):
        if direction == 'up':
            min_r = min(r for r, c in block)
            return [(r - min_r, c) for r, c in block]
        elif direction == 'left':
            min_c = min(c for r, c in block)
            return [(r, c - min_c) for r, c in block]

    blocks = find_blocks(grid)
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]

    for color, block in blocks:
        if color in [6, 7, 8]:
            shifted_block = shift_block(block, 'up')
        else:
            shifted_block = shift_block(block, 'left')
        for r, c in shifted_block:
            new_grid[r][c] = color

    return new_grid