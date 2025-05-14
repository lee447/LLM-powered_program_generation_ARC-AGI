from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_blocks(grid, target):
        blocks = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == target and (r, c) not in visited:
                    block = []
                    stack = [(r, c)]
                    while stack:
                        x, y = stack.pop()
                        if (x, y) not in visited and grid[x][y] == target:
                            visited.add((x, y))
                            block.append((x, y))
                            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                                    stack.append((nx, ny))
                    blocks.append(block)
        return blocks

    def fill_block(grid, block, color):
        for x, y in block:
            grid[x][y] = color

    def get_bounding_box(block):
        min_r = min(x for x, y in block)
        max_r = max(x for x, y in block)
        min_c = min(y for x, y in block)
        max_c = max(y for x, y in block)
        return min_r, max_r, min_c, max_c

    def fill_bounding_box(grid, min_r, max_r, min_c, max_c, color):
        for r in range(min_r, max_r + 1):
            for c in range(min_c, max_c + 1):
                grid[r][c] = color

    output = [row[:] for row in grid]
    blocks = find_blocks(grid, 1)
    for block in blocks:
        min_r, max_r, min_c, max_c = get_bounding_box(block)
        fill_bounding_box(output, min_r, max_r, min_c, max_c, 2)
        if len(block) > 1:
            fill_block(output, block, 8)
            if len(block) > 2:
                fill_block(output, block, 6)
    return output