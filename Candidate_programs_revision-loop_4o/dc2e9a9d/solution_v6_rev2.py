def solve(grid):
    def find_shapes(grid, color):
        shapes = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == color and (r, c) not in visited:
                    shape = []
                    stack = [(r, c)]
                    while stack:
                        x, y = stack.pop()
                        if (x, y) not in visited and grid[x][y] == color:
                            visited.add((x, y))
                            shape.append((x, y))
                            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                                    stack.append((nx, ny))
                    shapes.append(shape)
        return shapes

    def can_place_shape(grid, shape, dr, dc):
        for r, c in shape:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0):
                return False
        return True

    def place_shape(grid, shape, dr, dc, color):
        for r, c in shape:
            grid[r + dr][c + dc] = color

    output_grid = [row[:] for row in grid]
    shapes = find_shapes(grid, 3)
    colors = [1, 8]

    for i, shape in enumerate(shapes):
        color = colors[i % len(colors)]
        placed = False
        for dr in range(len(grid)):
            for dc in range(len(grid[0])):
                if can_place_shape(output_grid, shape, dr, dc):
                    place_shape(output_grid, shape, dr, dc, color)
                    placed = True
                    break
            if placed:
                break

    return output_grid