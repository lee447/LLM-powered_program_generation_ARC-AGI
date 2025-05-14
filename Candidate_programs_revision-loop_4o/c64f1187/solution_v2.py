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

    def transform_blocks(blocks):
        new_grid = [[0] * 14 for _ in range(8)]
        for color, block in blocks:
            min_r = min(r for r, c in block)
            min_c = min(c for r, c in block)
            for r, c in block:
                new_r = r - min_r
                new_c = c - min_c
                if new_r < len(new_grid) and new_c < len(new_grid[0]):
                    new_grid[new_r][new_c] = color
        return new_grid

    blocks = extract_blocks(grid)
    return transform_blocks(blocks)