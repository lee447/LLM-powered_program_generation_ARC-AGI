def solve(grid):
    def find_non_zero_areas(grid):
        areas = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 and (r, c) not in visited:
                    color = grid[r][c]
                    area = []
                    stack = [(r, c)]
                    while stack:
                        x, y = stack.pop()
                        if (x, y) not in visited and grid[x][y] == color:
                            visited.add((x, y))
                            area.append((x, y))
                            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                                    stack.append((nx, ny))
                    areas.append((color, area))
        return areas

    def move_areas_to_bottom(areas, grid):
        max_row = len(grid) - 1
        for color, area in areas:
            min_col = min(c for _, c in area)
            max_col = max(c for _, c in area)
            height = max_row - max(r for r, _ in area)
            for r, c in area:
                grid[r][c] = 0
            for r, c in area:
                grid[r + height][c] = color

    areas = find_non_zero_areas(grid)
    move_areas_to_bottom(areas, grid)
    return grid