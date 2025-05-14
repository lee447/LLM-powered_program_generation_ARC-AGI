def solve(grid):
    def extract_blocks(grid):
        blocks = []
        for i in range(0, len(grid), 4):
            for j in range(0, len(grid[0]), 6):
                block = [row[j:j+6] for row in grid[i:i+4]]
                blocks.append(block)
        return blocks

    def transform_block(block):
        for i in range(len(block)):
            for j in range(len(block[0])):
                if block[i][j] == 0:
                    block[i][j] = block[0][0]
        return block

    blocks = extract_blocks(grid)
    transformed_blocks = [transform_block(block) for block in blocks]

    result = []
    for i in range(0, len(transformed_blocks), 3):
        for row in range(4):
            result.append(transformed_blocks[i][row] + transformed_blocks[i+1][row] + transformed_blocks[i+2][row])
    return result