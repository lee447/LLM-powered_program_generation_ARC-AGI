def solve(grid):
    def find_blocks(grid, color):
        blocks = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == color and (r, c) not in visited:
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
                    blocks.append(block)
        return blocks

    def move_block(block, direction):
        if direction == 'right':
            return [(r, c + 1) for r, c in block]
        elif direction == 'down':
            return [(r + 1, c) for r, c in block]

    def can_move(block, direction):
        if direction == 'right':
            return all(c + 1 < len(grid[0]) and grid[r][c + 1] == 8 for r, c in block)
        elif direction == 'down':
            return all(r + 1 < len(grid) and grid[r + 1][c] == 8 for r, c in block)

    def apply_move(block, direction):
        for r, c in block:
            grid[r][c] = 8
        moved_block = move_block(block, direction)
        for r, c in moved_block:
            grid[r][c] = 2

    blocks = find_blocks(grid, 2)
    for block in blocks:
        while can_move(block, 'right'):
            apply_move(block, 'right')
            block = move_block(block, 'right')
        while can_move(block, 'down'):
            apply_move(block, 'down')
            block = move_block(block, 'down')

    return grid