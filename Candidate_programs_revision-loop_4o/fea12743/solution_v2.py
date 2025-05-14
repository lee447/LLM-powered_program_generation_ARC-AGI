def solve(grid):
    def find_blocks(grid):
        blocks = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    block = []
                    stack = [(r, c)]
                    while stack:
                        x, y = stack.pop()
                        if (x, y) not in block and grid[x][y] == 2:
                            block.append((x, y))
                            if x > 0: stack.append((x-1, y))
                            if x < len(grid)-1: stack.append((x+1, y))
                            if y > 0: stack.append((x, y-1))
                            if y < len(grid[0])-1: stack.append((x, y+1))
                    blocks.append(block)
        return blocks

    def color_block(grid, block, color):
        for x, y in block:
            grid[x][y] = color

    blocks = find_blocks(grid)
    colors = [8, 3, 2]
    for i, block in enumerate(blocks):
        color_block(grid, block, colors[i % len(colors)])
    return grid