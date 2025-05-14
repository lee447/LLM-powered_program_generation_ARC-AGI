def solve(grid):
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

    def place_blocks_on_bottom(grid, blocks):
        new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
        for color, block in blocks:
            min_r = min(r for r, c in block)
            max_r = max(r for r, c in block)
            min_c = min(c for r, c in block)
            max_c = max(c for r, c in block)
            height = max_r - min_r + 1
            width = max_c - min_c + 1
            bottom_r = len(grid) - height
            for r, c in block:
                new_r = bottom_r + (r - min_r)
                new_c = c
                new_grid[new_r][new_c] = color
        return new_grid

    blocks = find_non_zero_blocks(grid)
    blocks.sort(key=lambda x: (min(c for r, c in x[1]), min(r for r, c in x[1])))
    return place_blocks_on_bottom(grid, blocks)