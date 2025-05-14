def solve(grid):
    def extract_non_zero_block(grid):
        min_row, max_row = len(grid), 0
        min_col, max_col = len(grid[0]), 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
        return [row[min_col:max_col+1] for row in grid[min_row:max_row+1]]

    def find_largest_block(grid):
        blocks = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 and (r, c) not in visited:
                    color = grid[r][c]
                    stack = [(r, c)]
                    block = []
                    while stack:
                        x, y = stack.pop()
                        if (x, y) in visited or grid[x][y] != color:
                            continue
                        visited.add((x, y))
                        block.append((x, y))
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                                stack.append((nx, ny))
                    blocks.append(block)
        largest_block = max(blocks, key=len)
        min_row = min(x for x, y in largest_block)
        max_row = max(x for x, y in largest_block)
        min_col = min(y for x, y in largest_block)
        max_col = max(y for x, y in largest_block)
        result = [[0] * (max_col - min_col + 1) for _ in range(max_row - min_row + 1)]
        for x, y in largest_block:
            result[x - min_row][y - min_col] = grid[x][y]
        return result

    return find_largest_block(grid)