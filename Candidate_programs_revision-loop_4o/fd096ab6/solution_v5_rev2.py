from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_blocks(grid):
        blocks = []
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 1 and not visited[r][c]:
                    color = grid[r][c]
                    block = [(r, c)]
                    visited[r][c] = True
                    queue = [(r, c)]
                    while queue:
                        x, y = queue.pop(0)
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == color and not visited[nx][ny]:
                                visited[nx][ny] = True
                                block.append((nx, ny))
                                queue.append((nx, ny))
                    blocks.append((color, block))
        return blocks

    def expand_block(block, grid):
        color, cells = block
        min_r = min(cells, key=lambda x: x[0])[0]
        max_r = max(cells, key=lambda x: x[0])[0]
        min_c = min(cells, key=lambda x: x[1])[1]
        max_c = max(cells, key=lambda x: x[1])[1]
        for r in range(min_r, max_r + 1):
            for c in range(min_c, max_c + 1):
                if grid[r][c] == 1:
                    grid[r][c] = color

    blocks = find_blocks([row[:] for row in grid])
    for block in blocks:
        expand_block(block, grid)
    return grid