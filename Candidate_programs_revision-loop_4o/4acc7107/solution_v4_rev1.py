def solve(grid):
    def find_nonzero_blocks(grid):
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

    def shift_block(block, dr, dc):
        return [(r + dr, c + dc) for r, c in block]

    def place_block(grid, block, color):
        for r, c in block:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                grid[r][c] = color

    blocks = find_nonzero_blocks(grid)
    blocks.sort(key=lambda x: (x[1][0][0], x[1][0][1]))

    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1

    for i, (color, block) in enumerate(blocks):
        if i % 2 == 0:
            dr, dc = max_row - max(r for r, c in block), 0
        else:
            dr, dc = 0, max_col - max(c for r, c in block)
        shifted_block = shift_block(block, dr, dc)
        place_block(new_grid, shifted_block, color)

    return new_grid