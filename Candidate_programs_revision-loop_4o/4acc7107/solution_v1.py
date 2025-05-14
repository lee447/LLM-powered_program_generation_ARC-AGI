def solve(grid):
    def shift_down(grid, start_row, end_row, start_col, end_col):
        for r in range(end_row, start_row, -1):
            for c in range(start_col, end_col):
                grid[r][c] = grid[r-1][c]
        for c in range(start_col, end_col):
            grid[start_row][c] = 0

    def shift_right(grid, start_row, end_row, start_col, end_col):
        for r in range(start_row, end_row):
            for c in range(end_col, start_col, -1):
                grid[r][c] = grid[r][c-1]
        for r in range(start_row, end_row):
            grid[r][start_col] = 0

    def find_non_zero_blocks(grid):
        blocks = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 and (r, c) not in visited:
                    color = grid[r][c]
                    block = []
                    queue = [(r, c)]
                    while queue:
                        cr, cc = queue.pop(0)
                        if (cr, cc) in visited or grid[cr][cc] != color:
                            continue
                        visited.add((cr, cc))
                        block.append((cr, cc))
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                                queue.append((nr, nc))
                    blocks.append(block)
        return blocks

    blocks = find_non_zero_blocks(grid)
    for block in blocks:
        min_r = min(r for r, c in block)
        max_r = max(r for r, c in block)
        min_c = min(c for r, c in block)
        max_c = max(c for r, c in block)
        if max_r - min_r > max_c - min_c:
            shift_down(grid, min_r, max_r, min_c, max_c + 1)
        else:
            shift_right(grid, min_r, max_r + 1, min_c, max_c)

    return grid