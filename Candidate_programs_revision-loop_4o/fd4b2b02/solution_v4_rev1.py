from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_blocks(grid):
        blocks = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 and (r, c) not in visited:
                    color = grid[r][c]
                    block = []
                    queue = [(r, c)]
                    while queue:
                        x, y = queue.pop(0)
                        if (x, y) not in visited and grid[x][y] == color:
                            visited.add((x, y))
                            block.append((x, y))
                            if x + 1 < len(grid):
                                queue.append((x + 1, y))
                            if y + 1 < len(grid[0]):
                                queue.append((x, y + 1))
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