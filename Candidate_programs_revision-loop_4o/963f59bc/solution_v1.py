from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_shapes(grid):
        shapes = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 and (r, c) not in visited:
                    color = grid[r][c]
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
                    shapes.append((color, shape))
        return shapes

    def move_shape(grid, shape, direction):
        color, cells = shape
        new_grid = [row[:] for row in grid]
        for r, c in cells:
            new_grid[r][c] = 0
        if direction == 'right':
            for r, c in cells:
                new_grid[r][c + 1] = color
        elif direction == 'down':
            for r, c in cells:
                new_grid[r + 1][c] = color
        return new_grid

    shapes = find_shapes(grid)
    for color, shape in shapes:
        if color == 1:
            grid = move_shape(grid, (color, shape), 'right')
        else:
            grid = move_shape(grid, (color, shape), 'down')
    return grid