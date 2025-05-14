from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_non_zero(grid):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    return r, c
        return None, None

    def extract_subgrid(grid, start_r, start_c):
        end_r, end_c = start_r, start_c
        while end_r < len(grid) and any(grid[end_r][c] != 0 for c in range(len(grid[0]))):
            end_r += 1
        while end_c < len(grid[0]) and any(grid[r][end_c] != 0 for r in range(len(grid))):
            end_c += 1
        return [row[start_c:end_c] for row in grid[start_r:end_r]]

    start_r, start_c = find_non_zero(grid)
    subgrid = extract_subgrid(grid, start_r, start_c)
    n = len(subgrid)
    m = len(subgrid[0])
    result = [[0] * (m + 2) for _ in range(n + 2)]

    for r in range(n):
        for c in range(m):
            result[r + 1][c + 1] = subgrid[r][c]

    border_color = result[1][1]
    for r in range(n + 2):
        result[r][0] = border_color
        result[r][m + 1] = border_color
    for c in range(m + 2):
        result[0][c] = border_color
        result[n + 1][c] = border_color

    return result