from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
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

    def draw_shape(grid, shape, color):
        for x, y in shape:
            grid[x][y] = color

    def get_bounding_box(shape):
        min_r = min(x for x, y in shape)
        max_r = max(x for x, y in shape)
        min_c = min(y for x, y in shape)
        max_c = max(y for x, y in shape)
        return min_r, max_r, min_c, max_c

    def translate_shape(shape, dr, dc):
        return [(x + dr, y + dc) for x, y in shape]

    output = [row[:] for row in grid]
    green_shapes = find_shapes(grid, 3)
    colors = [1, 8]

    for i, shape in enumerate(green_shapes):
        min_r, max_r, min_c, max_c = get_bounding_box(shape)
        if i < len(colors):
            color = colors[i]
            translated_shape = translate_shape(shape, 0, max_c - min_c + 1)
            if all(0 <= y < len(grid[0]) for x, y in translated_shape):
                draw_shape(output, translated_shape, color)
            else:
                translated_shape = translate_shape(shape, 0, -(max_c - min_c + 1))
                if all(0 <= y < len(grid[0]) for x, y in translated_shape):
                    draw_shape(output, translated_shape, color)

    return output