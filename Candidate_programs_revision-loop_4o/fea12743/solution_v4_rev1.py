def solve(grid):
    from collections import defaultdict, deque

    def find_blocks(grid, target_color):
        blocks = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == target_color and (r, c) not in visited:
                    block = []
                    queue = deque([(r, c)])
                    while queue:
                        x, y = queue.popleft()
                        if (x, y) not in visited and grid[x][y] == target_color:
                            visited.add((x, y))
                            block.append((x, y))
                            if x > 0: queue.append((x-1, y))
                            if x < len(grid)-1: queue.append((x+1, y))
                            if y > 0: queue.append((x, y-1))
                            if y < len(grid[0])-1: queue.append((x, y+1))
                    blocks.append(block)
        return blocks

    def color_block(grid, block, color):
        for x, y in block:
            grid[x][y] = color

    color_map = {8: 2, 3: 8, 2: 3}
    for original_color, new_color in color_map.items():
        blocks = find_blocks(grid, original_color)
        for block in blocks:
            color_block(grid, block, new_color)
    return grid