from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_blocks(grid, color):
        blocks = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == color:
                    if (r == 0 or grid[r-1][c] != color) and (c == 0 or grid[r][c-1] != color):
                        blocks.append((r, c))
        return blocks

    def fill_block(grid, start_r, start_c, new_color, original_color):
        for r in range(start_r, len(grid)):
            if grid[r][start_c] != original_color:
                break
            for c in range(start_c, len(grid[0])):
                if grid[r][c] != original_color:
                    break
                grid[r][c] = new_color

    colors = [8, 3, 2]
    for color in colors:
        blocks = find_blocks(grid, color)
        for r, c in blocks:
            fill_block(grid, r, c, colors[(colors.index(color) + 1) % len(colors)], color)
    
    return grid