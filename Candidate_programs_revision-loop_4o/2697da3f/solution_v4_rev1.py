def solve(grid):
    def rotate_90_clockwise(mat):
        return [[mat[j][i] for j in range(len(mat)-1, -1, -1)] for i in range(len(mat[0]))]

    def expand_grid(mat):
        n, m = len(mat), len(mat[0])
        new_grid = [[0] * (2 * m - 1) for _ in range(2 * n - 1)]
        for i in range(n):
            for j in range(m):
                new_grid[i][j] = mat[i][j]
                new_grid[i][j + m - 1] = mat[i][j]
                new_grid[i + n - 1][j] = mat[i][j]
                new_grid[i + n - 1][j + m - 1] = mat[i][j]
        return new_grid

    rotated_grid = rotate_90_clockwise(grid)
    expanded_grid = expand_grid(rotated_grid)
    return expanded_grid