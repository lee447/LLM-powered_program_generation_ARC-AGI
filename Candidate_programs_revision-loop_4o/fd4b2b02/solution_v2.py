def solve(grid):
    def find_blocks(grid):
        blocks = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    color = grid[r][c]
                    block = []
                    for i in range(r, len(grid)):
                        if grid[i][c] == color:
                            block.append((i, c))
                        else:
                            break
                    for j in range(c, len(grid[0])):
                        if grid[r][j] == color:
                            block.append((r, j))
                        else:
                            break
                    blocks.append((color, block))
        return blocks

    def place_blocks(grid, blocks):
        for color, block in blocks:
            for r, c in block:
                grid[r][c] = color

    blocks = find_blocks(grid)
    output_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    place_blocks(output_grid, blocks)
    return output_grid