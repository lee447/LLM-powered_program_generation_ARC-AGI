from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_color_areas(grid, color):
        areas = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == color and (r, c) not in visited:
                    stack = [(r, c)]
                    area = []
                    while stack:
                        x, y = stack.pop()
                        if (x, y) not in visited and grid[x][y] == color:
                            visited.add((x, y))
                            area.append((x, y))
                            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                                    stack.append((nx, ny))
                    areas.append(area)
        return areas

    def fill_area(grid, area, color):
        for x, y in area:
            grid[x][y] = color

    def transform(grid):
        new_grid = [row[:] for row in grid]
        blue_areas = find_color_areas(grid, 1)
        for area in blue_areas:
            fill_area(new_grid, area, 8)
        red_areas = find_color_areas(grid, 4)
        for area in red_areas:
            fill_area(new_grid, area, 2)
        return new_grid

    return transform(grid)