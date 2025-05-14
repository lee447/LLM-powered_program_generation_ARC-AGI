from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_red_blocks(grid):
        red_blocks = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    if (r == 0 or grid[r-1][c] != 2) and (c == 0 or grid[r][c-1] != 2):
                        red_blocks.append((r, c))
        return red_blocks

    def extend_red_block(grid, r, c):
        max_r, max_c = len(grid), len(grid[0])
        end_r, end_c = r, c
        while end_r < max_r and grid[end_r][c] == 2:
            end_r += 1
        while end_c < max_c and grid[r][end_c] == 2:
            end_c += 1
        return end_r - 1, end_c - 1

    def place_red_block(output, r1, c1, r2, c2):
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                output[r][c] = 2

    red_blocks = find_red_blocks(grid)
    output = [row[:] for row in grid]

    for r, c in red_blocks:
        r2, c2 = extend_red_block(grid, r, c)
        place_red_block(output, r, c, r2, c2)

    return output