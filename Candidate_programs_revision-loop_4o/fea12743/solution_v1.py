def solve(grid):
    def find_blocks(grid):
        blocks = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    if (r == 0 or grid[r-1][c] != 2) and (c == 0 or grid[r][c-1] != 2):
                        blocks.append((r, c))
        return blocks

    def fill_block(grid, start_r, start_c, new_color):
        for r in range(start_r, len(grid)):
            if grid[r][start_c] != 2:
                break
            for c in range(start_c, len(grid[0])):
                if grid[r][c] != 2:
                    break
                grid[r][c] = new_color

    blocks = find_blocks(grid)
    colors = [8, 3, 2]
    for i, (r, c) in enumerate(blocks):
        fill_block(grid, r, c, colors[i % len(colors)])
    
    return grid