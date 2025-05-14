def solve(grid):
    def extract_blocks(grid):
        blocks = []
        for i in range(0, len(grid), 4):
            for j in range(0, len(grid[0]), 6):
                block = [row[j:j+6] for row in grid[i:i+4]]
                blocks.append(block)
        return blocks

    def rotate_block(block):
        return [list(row) for row in zip(*block[::-1])]

    def transform_block(block):
        rotated = rotate_block(block)
        for i in range(len(rotated)):
            for j in range(len(rotated[0])):
                if rotated[i][j] == 0:
                    rotated[i][j] = block[0][0]
        return rotated

    blocks = extract_blocks(grid)
    transformed_blocks = [transform_block(block) for block in blocks]

    result = []
    for i in range(0, len(transformed_blocks), 3):
        for row in range(4):
            result.append(transformed_blocks[i][row] + transformed_blocks[i+1][row] + transformed_blocks[i+2][row])
    return result