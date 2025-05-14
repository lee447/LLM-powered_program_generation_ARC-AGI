from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_red_shape(grid):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    return r, c
        return None, None

    def get_shape_bounds(grid, start_r, start_c):
        min_r, max_r = start_r, start_r
        min_c, max_c = start_c, start_c
        stack = [(start_r, start_c)]
        visited = set(stack)
        while stack:
            r, c = stack.pop()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] == 2:
                    visited.add((nr, nc))
                    stack.append((nr, nc))
                    min_r, max_r = min(min_r, nr), max(max_r, nr)
                    min_c, max_c = min(min_c, nc), max(max_c, nc)
        return min_r, max_r, min_c, max_c

    def fill_pattern(grid, min_r, max_r, min_c, max_c):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if min_r <= r <= max_r and min_c <= c <= max_c:
                    if grid[r][c] == 2:
                        continue
                    if r == min_r or r == max_r or c == min_c or c == max_c:
                        grid[r][c] = 8
                    else:
                        grid[r][c] = 2
                else:
                    if (r + c) % 2 == 0:
                        grid[r][c] = 1
                    else:
                        grid[r][c] = 0

    start_r, start_c = find_red_shape(grid)
    if start_r is not None and start_c is not None:
        min_r, max_r, min_c, max_c = get_shape_bounds(grid, start_r, start_c)
        fill_pattern(grid, min_r, max_r, min_c, max_c)
    return grid