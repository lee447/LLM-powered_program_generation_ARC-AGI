from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_non_zero_blocks(grid):
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

    def move_block(block, dr, dc):
        return [(r + dr, c + dc) for r, c in block]

    def place_block(grid, block, color):
        for r, c in block:
            grid[r][c] = color

    blocks = find_non_zero_blocks(grid)
    blocks.sort(key=lambda x: (min(r for r, c in x[1]), min(c for r, c in x[1])))

    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for color, block in blocks:
        min_r = min(r for r, c in block)
        min_c = min(c for r, c in block)
        if min_r < len(grid) // 2:
            dr = len(grid) // 2 - min_r
        else:
            dr = -min_r
        if min_c < len(grid[0]) // 2:
            dc = len(grid[0]) // 2 - min_c
        else:
            dc = -min_c
        new_block = move_block(block, dr, dc)
        place_block(new_grid, new_block, color)

    return new_grid