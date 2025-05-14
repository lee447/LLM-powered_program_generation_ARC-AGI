def solve(grid):
    def extract_blocks(grid):
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
    return output_grid