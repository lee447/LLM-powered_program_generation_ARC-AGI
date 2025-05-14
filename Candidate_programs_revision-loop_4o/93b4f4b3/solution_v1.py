def solve(grid):
    def extract_subgrid(grid, start_row, start_col, height, width):
        return [row[start_col:start_col + width] for row in grid[start_row:start_row + height]]

    def find_subgrid(grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    return i, j
        return None, None

    def transform_subgrid(subgrid):
        n = len(subgrid)
        m = len(subgrid[0])
        transformed = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if subgrid[i][j] != 0:
                    transformed[i][j] = subgrid[i][j]
        return transformed

    def place_subgrid(grid, subgrid, start_row, start_col):
        for i in range(len(subgrid)):
            for j in range(len(subgrid[0])):
                grid[start_row + i][start_col + j] = subgrid[i][j]

    n = len(grid)
    m = len(grid[0])
    output_grid = [[0] * (m // 2) for _ in range(n)]
    for i in range(0, n, 4):
        for j in range(0, m, 6):
            subgrid = extract_subgrid(grid, i, j, 4, 6)
            start_row, start_col = find_subgrid(subgrid)
            if start_row is not None:
                transformed = transform_subgrid(subgrid)
                place_subgrid(output_grid, transformed, i, j // 2)
    return output_grid