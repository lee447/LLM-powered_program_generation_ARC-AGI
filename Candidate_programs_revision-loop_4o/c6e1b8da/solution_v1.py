def solve(grid):
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

    def adjust_block(block, grid):
        min_r = min(x for x, y in block)
        min_c = min(y for x, y in block)
        max_r = max(x for x, y in block)
        max_c = max(y for x, y in block)
        new_block = []
        for x, y in block:
            if x == min_r or x == max_r or y == min_c or y == max_c:
                new_block.append((x, y))
        return new_block

    blocks = find_blocks(grid)
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for color, block in blocks:
        adjusted_block = adjust_block(block, grid)
        for x, y in adjusted_block:
            new_grid[x][y] = color
    return new_grid